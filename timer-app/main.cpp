#include <iostream>
#include <stdlib.h>
#include <string.h>
#include <vector>

#include "timer.hpp"

using namespace std;

void test_vector_function() {

    vector<int> newVector = {15,4,6,8,94,6,8,94,6,8,94,8,94,6,8,94,6,8,94,6,8,94,6,8,94,6,8,94,6,8,94,6,8,94,6,8,94,6,8,94,6,8,94,6,8,94,6,8,94,6,8,94,6,8};
    for (short i = 0; i < newVector.size(); i++) {
        cout << newVector[i] << endl;
    }

    newVector.clear();
    // return !newVector.empty() ? newVector[0] : 0;
}

void hello() {
    // fast function, won't time well
   // cout << "Message" << endl;
}


int main() {

    init_time(hello);

    // should take longer than hello()
    init_time(test_vector_function);

    // init_time(cout);

   return 0;
}
