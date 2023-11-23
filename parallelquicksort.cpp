#include <iostream>
#include <vector>
#include <omp.h>
int k = 0;
// Function to partition the array
int partition(std::vector<int> &arr, int low, int high)
{
    int pivot = arr[high];
    int i = (low - 1);

    for (int j = low; j < high; j++)
    {
        if (arr[j] < pivot)
        {
            i++;
            std::swap(arr[i], arr[j]);
        }
    }

    std::swap(arr[i + 1], arr[high]);
    return (i + 1);
}

// Function to perform quicksort in parallel
void parallelQuickSort(std::vector<int> &arr, int low, int high)
{
    if (low < high)
    {
        int pivotIndex = partition(arr, low, high);
        int threadNum = omp_get_thread_num(); // Get the thread number

        // Print the pivot value and thread number
        std::cout << "\nThread " << k << " chose pivot " << arr[pivotIndex] << std::endl;

#pragma omp parallel sections
        {
#pragma omp section
            {
                k = k + 1;
                parallelQuickSort(arr, low, pivotIndex - 1);
            }
#pragma omp section
            {
                k = k + 1;
                parallelQuickSort(arr, pivotIndex + 1, high);
            }
        }
    }
}

int main()
{
    std::vector<int> arr = {9, 6, 3, 7, 2, 12, 5, 1};

    std::cout << "Original Array: ";
    for (int num : arr)
    {
        std::cout << num << " ";
    }

#pragma omp parallel
    {
#pragma omp single
        parallelQuickSort(arr, 0, arr.size() - 1);
    }

    std::cout << "\nSorted Array: ";
    for (int num : arr)
    {
        std::cout << num << " ";
    }

    return 0;
}

// g++ -fopenmp your_program.cpp -o your_program