l = [6,7,8,9,10,1,2,3,4,5];
even = [x for x in l if x%2 == 0];
odd = [x for x in l if x%2 != 0];
even.sort();
odd.sort();
print("Sorted even numbers:", even);
print("Sorted odd numbers:", odd);  