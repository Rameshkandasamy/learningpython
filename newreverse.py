a = str(raw_input("Enter your string to reverse order: "));
b = a.split();

c = list(reversed(b));

c = ' '.join(c);

print c;
