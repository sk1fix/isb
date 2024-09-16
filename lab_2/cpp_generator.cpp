#include <iostream>
#include <random>
#include <limits>

using namespace std;

/**
 * This function initializes the random number generator using the current time and generates
 * a 128-bit binary sequence, printing it to the standard output.
 *
 * @return None
 */
void generate()
{
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<int> distribution(numeric_limits<int>::min(), numeric_limits<int>::max());
    for (int i = 0; i < 128; i++)
    {
        cout << abs(distribution(gen)) % 2;
    }
}

int main()
{
    generate();
    return 0;
}