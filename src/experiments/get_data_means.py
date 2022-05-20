def NormalizeData(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))


def counter(npy_file, csv_file):
    def compute_EER(cosines_norm, matches):
        fpr, tpr, thresholds = metrics.roc_curve(matches, cosines_norm, pos_label=1)
        idxs = np.sort(np.where(thresholds > 1)).flatten()[::-1]
        if len(idxs) > 0:
            fpr = np.delete(fpr, idxs)
            tpr = np.delete(tpr, idxs)
            thresholds = np.delete(thresholds, idxs)
        eer = brentq(lambda x: 1. - x - interp1d(fpr, tpr)(x), 0., 1.)
        thresh = interp1d(fpr, thresholds)(eer)
        print(eer)
        return thresh

    errors_by_group = [[] for _ in range(6)]

    results = np.load(npy_file)
    results[:, 0] = NormalizeData(results[:, 0])
    t = compute_EER(results[:, 0], results[:, 1])
    print(t)
    with open(csv_file, "r") as csv:
        lines = csv.readlines()
    couples = []
    for i, line in enumerate(lines):
        data = line.split(",")
        try:
            r = [0, 0, 0, 0, i, 0]
            c1 = "/".join(data[0].split("/")[-2:])
            attributes = [f[c1][k] for k in keys]
            identity = c1.split("/")[0]
            group = int(results[i, 2])
            row = [identity]
            row.extend(attributes)
            ####################
            # counter data format : FR, FA, TR, TA
            ####################
            if results[i, 0] >= t and results[i, 1] == 1:
                r[3] = 1
            if results[i, 0] < t and results[i, 1] == 1:
                r[0] = 1
            if results[i, 0] >= t and results[i, 1] == 0:
                r[1] = 1
            if results[i, 0] < t and results[i, 1] == 0:
                r[2] = 1
            r[5] = results[i, 0]
            row.extend(r)
            errors_by_group[group].append(row)
        except:
            pass
    return errors_by_group