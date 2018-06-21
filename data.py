import func_utils
import main

from keras.models import Sequential
from keras.layers import Dense
import numpy as np

func = main.add

def run():
    # train model
    x_train, y_train = generate_samples(1000)
    model = create_model(x_train, y_train)

    # train on another batch
    #x_batch, y_batch = generate_samples(500)
    #train_batch(model, x_batch, y_batch)

    # evaluate model
    x_eval, y_eval = generate_samples(100)
    evaluate_model(model, x_eval, y_eval)


def generate_samples(sample_size):
    x = []
    y = []
    for i in range(sample_size):
        x_sample, y_sample = generate_good_sample()
        x.append(x_sample)
        y.append(y_sample)

    x = np.asanyarray(x)
    y = np.asanyarray(y)

    return x, y

def create_model(x_train, y_train):
    '''
    # create model
    model = Sequential()
    model.add(Dense(12, input_dim=2, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    # compile the model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    # fit the model
    model.fit(x_train, y_train, epochs=150, batch_size=10)
    '''

    model = Sequential()
    model.add(Dense(4, input_dim=2, activation='relu'))
    model.add(Dense(4, activation='relu'))
    model.add(Dense(1, activation='linear'))
    model.compile(loss='mse', optimizer='adam')
    model.fit(x_train, y_train, epochs=1000, verbose=0)

    return model


def evaluate_model(model, x_eval, y_eval):
    sample_size = len(x_eval)

    y_pred = model.predict(x_eval)
    print "starting evaluation"
    count = 0
    for i in range(sample_size):
        if abs(y_pred[i][0] - y_eval[i]) > 0.4:
            print y_pred[i][0], y_eval[i], x_eval[i]
            count += 1

    print "ending evaluation. precision rate is: %.2f" % ((sample_size - count) * 100 / sample_size)

def train_batch(model, x_batch, y_batch):
    print model.train_on_batch(x_batch, y_batch)

def generate_good_sample():
    return func_utils.execute(func)

def generate_bad_sample():
    sample = func_utils.execute(func)
    sample[-1] = func_utils.generate_param()
    return sample