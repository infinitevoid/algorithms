

template<class T>
void selection_sort(T array[], int n)
{
    for(int i = 0; i < n - 1; i++)
    {
        T max = array[i+1];
        int max_index = i+1;
        for(int j = i + 2; j < n; j++)
        {
            if(array[j] > max)
            {
                max = array[j]; 
                max_index = j;
            }
        }
        array[max_index] = array[i];
        array[i] = max;
    }
}