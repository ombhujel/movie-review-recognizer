How to run this code:
The zipfile already contains the necessary files so, one can only run the LR.py, to obtain the result, however, if all files are processed, 
it'll just overwrite the existing files.

The two scripts are already well defined, so one only need to put the train folder containing
the negative and positove reviews and the test folder containing the negative reviews in the 
same directory and run the pre_process.py first and merge.py second and lastly LR.py. 


Detail description:

There are two scripts, the pre process main job is to convert both training example and test example to the 
feature vector format, so that the other script “LR” could perform SGD and then calculate the efficiency of
 the model on the test example.
There are three main function on the pre process script, namely, stemming, most_frequency and convert_into_vector. 
As name suggests, the job of stemming is to read through all the text file, given the path as parameter. It does 
so by first lowering the words and removing the punctuations and stop words, and then again join, and finally write
in the file, one review at a time. It stores all the vocabularies of positive and negative in one file for training
and another file for test.
The second function, again as name suggested, will count the frequency of the words in the in the vocabulary file
 and store the top 10 or 100 or 300 on the respective list. 
The final function converts the review into vector, half way of the function steps are same as stemming,
 up to extracting punctuations, and then it goes on the loop of list containing most frequent words, and if 
the words appear on the review, it writes 1 on the vector file and “break” on that cycle, and if the word doesn’t 
appear, it writes 0 at the end of that loop cycle. The loop ends once it goes through all the most frequent words in
the list.
These are the only functions in this script and with proper file initialization, the final vector is achieved.

The other script LR, contains several functions, but the main function is SGD, which calculates the weight vector for the input and other functions can be considered sub functions of this main function. Like, z_calc function jobs is to calculate the z score, and y_prime’s job is to calculate the sigmoid of z, and similarly, cross entropy’s job is to calculate the cross entropy loss of the model. There are two more function, LR classifier, which calculates the sigmoid of z score on the test example and the writes the output on the file, one example at a time, and the accuracy function, at last, computes the accuracy of the model. There’s one more function called generator, which is built in order to get the flexibility of java’s hasnext() function, which gives next character before whitespace from the file each time its called, which is used to read the input vectors, one at a time.

The train_folder_positive and train_folder_negative and test_folder positive and test_folder_negative creates the path 
to the actual text files containing reviews. Since we have to use the read+operation, we first create the file with 
write and then close it instantly and then finally use read+ to start writing on the file without overwriting.
Since this model will create the feature vector of size 10, 100 and 300, we create the respective files. The reason 
to create positive and negative file separately is because for some reason while using the feature vector for stochastic
 gradient descent, different parameters were obtained, so there is a new script called merge.py which basically merge 
two files one line from negative review and one line from the positive review, so that we get the alternate review every 
time it goes through the gradient descent. However, this is only done for training input, because on test we’re going
through all the input anyway.
So for test data, there’s only three files created of respective sizes.

Then the respective files path are passed to the stemming function, to create a file containing all the 
vocabulary on the training file, I also did it with the test file but later realized since we’re creating 
the feature vector based on the training example vocabulary, the test vocabulary was not necessary. 

Then we pass the file containing all the vocabulary to the most_frequency function and create a list of 10 most,
 100 most and 300 most frequent words. 
Finally we go through all the actual text files again and then using the list of most frequent words we create 
the input vector one example at a time for the LR.py to perform on. As mentioned above, there are two separate 
file created for each size for training example, so that we can later merge them together in an alternating sequence. 
However only one file of each size for the test data.

LR. Py

The words_10_train, and words_10_test, when instantiated with next() will read one word at a time from the destined file,
 and the word in our case is 0s and 1s. So we basically perform the stochastic gradient descent one example at a time 
until the loss function is less than 0.01, during the process, we update the weight parameter and bias which will be
 used later by the LR_classifier function to predict the movie review using the test input data and the respective
 weight vector, and of course bias. And we write the actual label and predicted label in the file named 
output_file_accuracy_.txt, which is closed after the LR_classifier is done, so that it can read on that file to perform the accuracy later on.

The hyper parameter was selected 0.7 because it gave the most accuracy on size 100 and 300 on trining data, so we saved hyper parameter to be 0.7.
"# movie-review-recognizer" 
"# movie-review-recognizer" 
