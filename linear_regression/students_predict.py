from linear_regression.linear_model import build_model, load_model, test_model

if __name__ == "__main__":
    # build_model('resources/student-mat.csv',
    #             'G3',
    #             ["G1", "G2", "G3", "studytime", "failures", "absences"],
    #             # save_to='models/student_grades',
    #             iterate=100,
    #             test=True,
    #             test_size=0.1,
    #             plot=False,
    #             plot_by='G1',
    #             separator=';',
    #             output=['accuracy', 'data', 'iterations'])

    model = load_model('models/student_grades_0.9393486947104989.pickle')
    test_vector = [5, 5, 3, 1, 2]
    test_model(model, test_vector)
