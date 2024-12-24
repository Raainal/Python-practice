'''n=int(input("Enter number of rows "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(64+i),end=" ")
    print()


n=int(input("Enter number of rows "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(chr(65+n+i),end=" ")
    print()
    
'''

'''
in java 
public class pattern_new {
    public static void main(String[] args)
    {
        for (int a=65;a<=70;a++)
        {

            for (int i=65;i<=a;i++)
            {
                char ch=(char)i;
                System.out.print(ch);
            }
            System.out.println("");
        }

        for (int a=70;a>=65;a--)
        {

            for (int i=65;i<=a;i++)
            {
                char ch=(char)i;
                System.out.print(ch);
            }
            System.out.println("");
        }
    }
    
}

'''


for i in range(0,4):
    for j in range(0,1+i):
        print(chr(65+j),end=" ")
    print()

for i in range(0,4):
    for j in range(0,4-i):
        print(chr(65+j),end=" ")
    print()