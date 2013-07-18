<Query Kind="Program">
</Query>

void Main()
{
	string input = @"32 12
142341 512345
65535 4294967295";
	input.Split(new string[] { "\r\n" }, StringSplitOptions.None).ToList().ForEach(line =>
	{
		string[] inputs = line.Split(' ');
		FindGreatestCommonDivisor(uint.Parse(inputs[0]), uint.Parse(inputs[1])).Dump();;
	});

	
}

public static uint FindGreatestCommonDivisor(uint i1, uint i2)
{
	uint remainder = i1 % i2;
	return remainder == 0 ? i2 : FindGreatestCommonDivisor(i2, remainder);
}
