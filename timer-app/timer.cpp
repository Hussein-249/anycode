#include <iostream>
#include <thread>
#include <numeric> // for finding the sum of a vector
#include <mutex>
#include "timer.hpp"

std::mutex mutx;


void init_time(funcptr function) {

    std::vector<int>            times;
    std::vector<std::thread>    threads; // need to add threads to a vector to join all
    short size;

    timer_msg_start();

    for (short i = 0; i < 50; i++) {
        std::thread newThread(timeThread, function, std::ref(times));

        threads.push_back(std::move(newThread));
    }

    size = threads.size();


    for (std::thread &thr : threads) {
        thr.join();
    }

    display_runtime(times, size);

    timer_msg_end();
}


void timeThread(funcptr function, std::vector<int> &times) {


    auto start_time = std::chrono::high_resolution_clock::now();

    function();

    auto end_time = std::chrono::high_resolution_clock::now();

    auto function_runtime = std::chrono::duration_cast<std::chrono::microseconds>(end_time - start_time);

    int microseconds = function_runtime.count();

    mutx.lock();

    times.push_back(microseconds);

    mutx.unlock();
}


void timer_msg_start() {

    std::cout << "-------------------------------------------" << std::endl;

    std::cout << "Executing function: " << __func__ << std::endl;
}

void display_runtime(std::vector<int> &times, short &size) {

    float sum = std::accumulate(times.begin(), times.end(), 0);

    float avg = sum / size;

    float avg_seconds = avg / 100000.0;

    std::cout << "Function timed over " << size << " successful threads." << std::endl;

    std::cout << "Average duration: " << avg << std::endl << "Seconds: " << avg_seconds << std::endl;

}


void timer_msg_end() {

    std::cout << "Function : " << __func__ << " Completed" << std::endl;

    std::cout << "-------------------------------------------" << std::endl;
}
