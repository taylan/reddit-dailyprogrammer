File.ReadLines(@"input.txt")
	.Select (l => l.Split(new []{' '}, StringSplitOptions.RemoveEmptyEntries))
	.Where (a => a.Length == 3  && (a[0] == "0" || a[0] == "1"))
	.Select (a => (a[0] == "0" ? a[1].ToList().Aggregate (string.Empty, (current, reversed) => reversed + current) : a[1].ToUpper()) == a[2] ? "Good test data" : "Mismatch! Bad test data")
	.ToList().ForEach(s => Console.WriteLine(s));