Utility to read and serialize mnist datasets

mnist.py is the main class for reading, serialize and deserialize the datasets. It is more time effective to use a serialized dataset but it is possible to use the raw dataset only if prefered.
If no serialized dataset exists, call serializeDataSet with the raw datasets in the specified location. This create a serialized dataset with pickle with can be used by calling deserializeData.

svn.py is an (non effective) summport vector machine to demonstrate the handling of the datasets

The data directory contains the raw datasets from http://yann.lecun.com/exdb/mnist/ and also a pickle serialized set 