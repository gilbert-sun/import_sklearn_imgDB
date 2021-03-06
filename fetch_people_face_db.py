# -- coding: utf-8 --
from import_sklearn_imgDB.sklearn_data import fetch_people_datasets


def main():

    db1="./casia_part"
    db2="/home/gilbert0/Documents/2017-12-13-AI/icyface_offline/data/CASIA-WebFace/"

    # path: db1="/home/.../CASIA-WebFace" , resolution : w:64  h:64 , nPer: 3 persons
    X, y, z = fetch_people_datasets(db1, 64, 64, 3, False)

    ''' path: "/home/..." , resolution : w:64  h:64 , nPer: 25 persons
    #X, y, z = fetch_people_datasets(db2, 64, 64, 25, False)'''
    n_samples, n_features = X.shape

    print("n_samples: {}".format(n_samples))
    print("n_features: {}".format(n_features))

    print(len(set(list(z))))
    print(set(list(z)))


if __name__ == '__main__':
    main()