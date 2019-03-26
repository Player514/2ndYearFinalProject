import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Flatten, LSTM, Conv1D, MaxPooling1D, Dropout, Bidirectional, Embedding, Flatten, Activation
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from tensorflow.keras import optimizers

def fnn_embed(maxlen, num_label, optimizer, units = 60, activation = "relu",loss='sparse_categorical_crossentropy', embed_dim = 20, vocab_size = 445,metrics=['accuracy']):


    maxlen = maxlen

    model = Sequential()
    model.add(Embedding(input_dim=vocab_size, 
                    output_dim=32, 
                    input_length=maxlen))
    model.add(Flatten())
    model.add(Dense(units, input_dim=maxlen, activation=activation))
    model.add(Dense(units, input_dim=units, activation=activation))
    model.add(Dense(num_label, input_dim=units, activation='softmax')) 
    model.compile(optimizer=optimizer, loss=loss, metrics=metrics) 
    model.summary()
    return model

				 
tf.keras.optimizers.Adam	
	
optimizer = optimizers.adam(lr=0.0005)
model = fnn_embed(maxlen,train_labels_vec.shape[1],optimizer=optimizer)

hist = model.fit(train_padded_docs, 
                 train_labels_array, 
                 validation_data=(dev_padded_docs,dev_labels_array),
                 epochs=40, 
                 batch_size=20)
