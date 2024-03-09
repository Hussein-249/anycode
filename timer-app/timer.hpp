#ifndef TIMER_HPP
#define TIMER_HPP
#include <chrono> // for retrieving current time
#include <string>
#include <sstream>
#include <vector>


typedef void (*funcptr)(); // pointer to a void function

/*
 * @brief
 *
 * @param a pointer to the function to be timed.
 *
 * This function creates 20 threads to be executed concurrently
 * These threads are timed and then the times are passed on to calculate an average runtime.
 */
void init_time(funcptr function);

/*
 * @brief Where the function is called and timed.
 *
 * @param a pointer to the function to be timed, a reference to a vector to store runtimes
 *
 * This function gets the current time, exectues the function pointer,
 * and then gets the time again once the function has been executed.
 */
void timeThread(funcptr function, std::vector<int> &times);


void timer_msg_start();


void display_runtime(std::vector<int> &times, short &size);


void timer_msg_end();


#endif
