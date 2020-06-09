from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import numpy as np
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Embedding, Dense, LSTM, SimpleRNN

text = open('trainData.txt', 'rb').read().decode(encoding='utf-8')
text = text.split('\r')
f = open('first_text.txt', 'w', -1, 'utf-8')
f2 = open('last_text.txt', 'w', -1, 'utf-8')
for stri in text :
    stri = stri.split(' ')
    f.write(stri[0])
    f2.write(stri[-1].replace('.','\r'))
f.close()
f2.close()

for i in range(len(text)) :
    text[i] = text[i].replace('\n','')

t = Tokenizer()
t.fit_on_texts(text)
print(text)
vocab_size = len(t.word_index) + 1
print(text)
print('단어 집합의 크기 : %d' % vocab_size)
sequences = list()

for line in text:
    encoded = t.texts_to_sequences([line], )[0]
    for i in range(1, len(encoded)):
        sequence = encoded[:i+1]
        sequences.append(sequence)


max_len=max(len(l) for l in sequences)
print('샘플의 최대 길이 : {}'.format(max_len))
sequences = pad_sequences(sequences, maxlen=max_len, padding='pre')
print(sequences[:3])
sequences = np.array(sequences)
print(sequences)

X = sequences[:,:-1]
y = sequences[:,-1]
y = to_categorical(y, num_classes=vocab_size)


model = Sequential()
model.add(Embedding(vocab_size, 10, input_length=max_len-1))
model.add(LSTM(128))
model.add(Dense(vocab_size, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, y, epochs=100, verbose=2)

model.save('LSTM_TRAIN33')


'''
model = Sequential()
model.add(Embedding(vocab_size, 10, input_length=max_len-1))
#model.add(LSTM(16, return_sequences=True))
#model.add(LSTM(32, return_sequences=True))
model.add(LSTM(64, return_sequences=True))
model.add(LSTM(128, return_sequences=False))
model.add(Dense(vocab_size, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, y, epochs=200, verbose=2)

model.save('LSTM_TRAIN2')
'''

'''
model = Sequential()
model.add(Embedding(vocab_size, 10, input_length=max_len-1))
model.add(LSTM(128, return_sequences=True))
model.add(LSTM(128, return_sequences=True))
model.add(LSTM(128, return_sequences=True))
model.add(LSTM(128, return_sequences=False))
model.add(Dense(vocab_size, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, y, epochs=200, verbose=2)

model.save('LSTM_TRAIN3')
'''

'''
model = Sequential()
model.add(Embedding(vocab_size, 10, input_length=max_len-1))
model.add(LSTM(128, return_sequences=True))
model.add(SimpleRNN(128))
model.add(Dense(vocab_size, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, y, epochs=200, verbose=2)

model.save('DEEP_RNN_TRAIN')
'''

'''
model = Sequential()
model.add(Embedding(vocab_size, 10, input_length=max_len-1))
#model.add(LSTM(128, return_sequences=True))
#model.add(LSTM(128, return_sequences=True))
model.add(LSTM(128, return_sequences=True))
model.add(LSTM(128, return_sequences=True))
model.add(SimpleRNN(128))
model.add(Dense(vocab_size, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, y, epochs=200, verbose=2)

model.save('deepRNN')
'''
