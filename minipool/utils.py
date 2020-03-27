import ujson as json
import pickle


def to_json(out_fname, data):
    with open(out_fname, "w") as wopen:
        json.dump(data, wopen, indent=4)
        # pickle.dump(data, wopen)


def from_json(fname):
    with open(fname, "r") as ropen:
        data = json.load(ropen)
        # data = pickle.load(ropen)
    return data


def to_pickle(out_fname, data):
    with open(out_fname, "wb") as wopen:
        # json.dump(data, wopen, indent=4)
        pickle.dump(data, wopen)


def from_pickle(fname):
    with open(fname, "rb") as ropen:
        # data = json.load(ropen)
        data = pickle.load(ropen)
    return data
