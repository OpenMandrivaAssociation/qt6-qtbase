// Extra PGO trainer for QByteArray / QSet. The upstream benches miss
// chained toUpper().toLower() (the remaining QByteArray hole) and only
// exercise 1e6-element QSet::intersect.
#include <QByteArray>
#include <QSet>
#include <QString>
#include <cstdint>

static volatile std::intptr_t sink;

static void ba_case_chain(QByteArray in, bool detach)
{
	if (detach)
		in.detach();
	const auto a = in.toUpper();
	const auto b = in.toLower();
	const auto c = in.toUpper().toLower();
	const auto d = in.toLower().toUpper();
	sink += a.size() + b.size() + c.size() + d.size();
}

int main()
{
	QByteArray sample;
	sample.reserve(8192);
	for (int i = 0; i < 4096; ++i)
		sample += char('a' + (i % 26));
	QByteArray mixed = sample;
	for (int i = 0; i < mixed.size(); i += 3)
		mixed[i] = char(uchar(mixed[i]) & ~0x20);

	for (int rep = 0; rep < 400; ++rep) {
		ba_case_chain(sample, false);
		ba_case_chain(sample, true);
		ba_case_chain(mixed, false);
		ba_case_chain(mixed, true);
	}

	for (int sz : {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000}) {
		QByteArray chunk(sz, 'x');
		for (int i = 0; i < 6; ++i) {
			QByteArray ba;
			ba.append(chunk);
			ba.prepend(chunk.left(qMin(sz, 64)));
			sink += ba.size();
		}
	}

	for (int rep = 0; rep < 80; ++rep) {
		QByteArray ba;
		ba.reserve(1 << 16);
		for (int i = 0; i < 2000; ++i)
			ba.append("key=value;");
		sink += ba.indexOf("value");
		sink += int(ba.contains("key"));
		ba.replace("value", "VAL");
		sink += ba.split(';').size();
		sink += QByteArray::number(rep).toLongLong();
		sink += int(QByteArray("-17").toULongLong());
		sink += QByteArray("1234567890").toULongLong();
		sink += ba.toPercentEncoding().size();
	}

	for (int n : {16, 64, 256, 1024, 4096, 16384, 65536, 262144}) {
		QSet<int> s;
		s.reserve(n);
		for (int i = 0; i < n; ++i)
			s.insert(i);
		int hits = 0;
		for (int i = 0; i < n; i += 3)
			hits += int(s.contains(i));
		for (int i = 0; i < n; i += 5)
			s.remove(i);
		int sum = 0;
		for (int v : s)
			sum += v;
		sink += hits + sum + s.size();
	}

	QSet<QString> names;
	names.reserve(4000);
	for (int i = 0; i < 4000; ++i)
		names.insert(QStringLiteral("item-") + QString::number(i));
	sink += int(names.contains(QStringLiteral("item-17")));

	// Modest set algebra — same ops as the bench, sizes that finish.
	for (int n : {256, 1024, 4096, 16384}) {
		QSet<int> a, b;
		a.reserve(n);
		b.reserve(n);
		for (int i = 0; i < n; ++i)
			a.insert(i);
		for (int i = n / 2; i < n + n / 2; ++i)
			b.insert(i);
		sink += QSet(a).unite(b).size();
		sink += QSet(a).intersect(b).size();
		sink += QSet(a).subtract(b).size();
	}

	return 0;
}
