import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib.pyplot as plt
from matplotlib import style
import pickle


style.use("ggplot")


def import_data(file_path, output=[], separator=','):
    data = pd.read_csv(file_path, sep=separator)

    if 'data' in output:
        print(f'============================')
        print(f'Data sample:')
        print(f'----------------------------')
        print(f'{data.head()}')
        print(f'============================')

    return data


def prep_data(_data, _predict, _labels, data_shuffle=True):
    _data = _data[_labels]
    if data_shuffle:
        _data = shuffle(_data)
    x = np.array(_data.drop([_predict], 1))
    y = np.array(_data[_predict])
    return _data, x, y


def train_model(target_feature_data, features_data, iterations=1, test_size=0.1, save_to=None, output=[]):
    best_accuracy = 0
    best_model = None
    linear = None
    for i in range(iterations):
        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(target_feature_data,
                                                                                    features_data,
                                                                                    test_size=test_size)
        linear = linear_model.LinearRegression()
        linear.fit(x_train, y_train)
        accuracy = linear.score(x_test, y_test)

        if 'iterations' in output:
            print('============================')
            print(f'Model {i} stats:')
            print(f'----------------------------')
            print('Accuracy:', accuracy)
            print('Coefficient: ', linear.coef_)
            print('Intercept: ', linear.intercept_)
            print('============================')

        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_model = linear

    if save_to:
        with open(f'{save_to}_{best_accuracy}.pickle', "wb") as f:
            pickle.dump(best_model, f)

    if 'accuracy' in output:
        print('============================')
        print(f'Best Accuracy = {best_accuracy}')
        print('============================')

    if linear:
        return linear
    else:
        raise Exception('failed to create model')


def load_model(file_path):
    return pickle.load(open(file_path, "rb"))


def test_model(model, target_feature_data, features_data, test_size=0.1):
    _, x_test, _, y_test = sklearn.model_selection.train_test_split(target_feature_data,
                                                                    features_data,
                                                                    test_size=test_size)
    print('============================')
    print('Model test:')
    predictions = model.predict(x_test)
    for x in range(len(predictions)):
        print(f'----------------------------')
        print(f'{x + 1}:')
        print(f'\tFeatures: {x_test[x]}')
        print(f'\tPredicted: {round(predictions[x], 2)}, Got: {y_test[x]}')
    print('============================')


def plot_data(data, x_axis, y_axis):
    plt.scatter(data[x_axis], data[y_axis])
    plt.legend(loc=4)
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.show()


def build_model(data_file,
                target_feature_key,
                features_keys,
                iterate=1,
                save_to=None,
                test=True,
                test_size=0.1,
                plot=False,
                plot_by=None,
                output=[],
                separator=',',
                data_shuffle=True):

    raw_data = import_data(data_file, output, separator)

    data, target_feature_data, features_data = prep_data(raw_data,
                                                         target_feature_key,
                                                         features_keys,
                                                         data_shuffle)

    model = train_model(target_feature_data,
                        features_data,
                        iterations=iterate,
                        test_size=0.1,
                        save_to=save_to,
                        output=output)

    if test:
        test_model(model,
                   target_feature_data,
                   features_data,
                   test_size=test_size)

    if plot:
        plot_data(data,
                  target_feature_key,
                  plot_by)


if __name__ == "__main__":
    build_model('resources/student-mat.csv',
                'G3',
                ["G1", "G2", "G3", "studytime", "failures", "absences"],
                # save_to='models/student_grades',
                iterate=100,
                test=True,
                test_size=0.1,
                plot=False,
                plot_by='G1',
                separator=';',
                output=['accuracy', 'data', 'iterations'])

    # model = load_model('student_grades_0.9393486947104989.pickle')
