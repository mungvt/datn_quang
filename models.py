import os
import pickle
import time
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from data_preprocessing import prepare_data, normalize_data_predict, normalize_data
import itertools
import matplotlib.pyplot as plt
import numpy as np


def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1, keepdims = True)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')


def train_model(model, X_train, y_train, model_name, model_dir='model'):
    if not os.path.exists(model_dir):
        os.mkdir(model_dir)

    start = time.time()
    model.fit(X_train, y_train)
    print("Finished training within {:.2f} seconds".format(time.time() - start))

    model_dest_path = os.path.join(model_dir, model_name + '.pkl')
    print("path of model: ", model_dest_path)
    # save model
    pickle.dump(model, open(model_dest_path, 'wb'))

    return model, model_dest_path


def load_model(model_path):
    loaded_model = pickle.load(open(model_path, 'rb'))

    return loaded_model


def predict_model(model, X_test):
    y_logit = model.predict(X_test)
    y_logit_prob = model.predict_proba(X_test)

    return y_logit, y_logit_prob


def run_models():
    X_train, X_test, y_train, y_test = normalize_data()

    RF_model = RandomForestClassifier(n_estimators=100, random_state=42)
    RF_model, RF_model_dest_path = train_model(RF_model, X_train, y_train, 'RF_model')

    # evaluate test
    RF_y_logit_test, RF_y_logit_prob_test = predict_model(RF_model, X_test)
    cm = confusion_matrix(y_test, RF_y_logit_test)
    class_names = ["Tốt", "Đạt", "Kém"]
    plt.figure()
    plot_confusion_matrix(cm, classes=class_names, title='Confusion matrix, without normalization')
    plt.savefig('static/img/RF.png')

    LR_model = LogisticRegression()
    LR_model, LR_model_dest_path = train_model(LR_model, X_train, y_train, 'LR_model')
    LR_y_logit_test, LR_y_logit_prob_test = predict_model(LR_model, X_test)
    cm = confusion_matrix(y_test, LR_y_logit_test)
    plt.figure()
    plot_confusion_matrix(cm, classes=class_names, title='Confusion matrix, without normalization')
    plt.savefig('static/img/LR.png')

    SVC_model = LinearSVC()
    SVC_model, SVC_model_dest_path = train_model(SVC_model, X_train, y_train, 'SVM_model')
    SVC_y_test = SVC_model.predict(X_test)
    cm = confusion_matrix(y_test, SVC_y_test)
    plt.figure()
    plot_confusion_matrix(cm, classes=class_names, title='Confusion matrix, without normalization')
    plt.savefig('static/img/SVM.png')

    KNN_model = KNeighborsClassifier(n_neighbors=5)
    KNN_model, KNN_model_dest_path = train_model(KNN_model, X_train, y_train, 'KNN_model')
    KNN_y_logit_test, LR_y_logit_prob_test = predict_model(KNN_model, X_test)
    cm = confusion_matrix(y_test, KNN_y_logit_test)
    plt.figure()
    plot_confusion_matrix(cm, classes=class_names, title='Confusion matrix, without normalization')
    plt.savefig('static/img/KNN.png')


def predict_one_test(x, model):
    x_std = normalize_data_predict(x)
    model_path = 'model/'
    if model == 0:
        model_path += 'KNN_model.pkl'
    elif model == 1:
        model_path += 'LR_model.pkl'
    elif model == 2:
        print('test')
        model_path += 'RF_model.pkl'
    elif model == 3:
        model_path += 'SVM_model.pkl'
    else:
        model_path = 'model/RF_model.pkl'

    model = load_model(model_path)
    result = model.predict(x_std)
    return result

run_models()