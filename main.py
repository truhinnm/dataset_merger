import os
import shutil


def area_check(xmin, ymin, xmax, ymax):
    if abs((xmin - xmax) * (ymin - ymax)) > 0.3:
        return False
    return True


if __name__ == '__main__':
    dataset_list = ["cbd", "enye", "ssli", "vd", "orig"]
    folder_list = ["test", "train", "valid"]
    cbd_list = ['Car']
    enye_list = ['Bbus', 'Bcar', 'Bicycle', 'Bmotorcycle', 'Btruck', 'Bus', 'Car',
                 'Motorcycle', 'Person', 'Segway', 'Skateboard', 'Taxi', 'Truck', 'Van']
    ssli_list = ['bicycle', 'bus', 'car', 'motorcycle', 'person', 'truck', 'umbrella']
    vd_list = ['Bus', 'Car', 'Motor Cycle', 'Person', 'Rickshaw', 'Truck']
    orig_list = ['bicycle', 'bus', 'car', 'motorbike', 'person']
    all_labels = ['bicycle', 'bus', 'car', 'motorbike', 'person', 'truck']

    for dataset in dataset_list:
        for folder in folder_list:
            for root, dirs, files in os.walk(dataset + '/' + folder + '/labels'):
                for file in files:
                    with open(dataset + '/' + folder + '/labels/' + file, 'r') as label:
                        ifempty = True
                        verdict = True
                        labels = []
                        while True:
                            line = label.readline()
                            if not line:
                                if ifempty:
                                    verdict = True
                                    break
                                break
                            else:
                                ifempty = False
                                values = line.split(' ')
                                labels.append(values)
                                if not area_check(float(values[1]), float(values[2]), float(values[3]), float(values[4])):
                                    print('bruh')
                                    verdict = False
                                    break
                        if verdict:
                            match dataset:
                                case "cbd":
                                    with open('complete/' + folder + '/labels/' + file, "w") as copy:
                                        for line in labels:
                                            line[0] = "2"
                                            copy.write(' '.join(line))
                                    img_name = file[:-3] + 'jpg'
                                    shutil.copy2(dataset + '/' + folder + '/images/' + img_name,
                                                 'complete/' + folder + '/images/' + img_name)
                                case "enye":
                                    with open('complete/' + folder + '/labels/' + file, "w") as copy:
                                        nonvalid = False
                                        for line in labels:
                                            match line[0]:
                                                case "2":
                                                    line[0] = "0"
                                                    copy.write(' '.join(line))
                                                case "5":
                                                    line[0] = "1"
                                                    copy.write(' '.join(line))
                                                case "6":
                                                    line[0] = "2"
                                                    copy.write(' '.join(line))
                                                case "7":
                                                    line[0] = "3"
                                                    copy.write(' '.join(line))
                                                case "8":
                                                    line[0] = "4"
                                                    copy.write(' '.join(line))
                                                case "11":
                                                    line[0] = "2"
                                                    copy.write(' '.join(line))
                                                case "12":
                                                    line[0] = "5"
                                                    copy.write(' '.join(line))
                                                case "13":
                                                    line[0] = "1"
                                                    copy.write(' '.join(line))
                                                case _:
                                                    nonvalid = True
                                                    break
                                        if nonvalid:
                                            print(file)
                                            copy.close()
                                            os.remove('complete/' + folder + '/labels/' + file)
                                        else:
                                            img_name = file[:-3] + 'jpg'
                                            shutil.copy2(dataset + '/' + folder + '/images/' + img_name,
                                                         'complete/' + folder + '/images/' + img_name)
                                case "orig":
                                    shutil.copy2(dataset + '/' + folder + '/labels/' + file,
                                                 'complete/' + folder + '/labels/' + file)
                                    img_name = file[:-3] + 'jpg'
                                    shutil.copy2(dataset + '/' + folder + '/images/' + img_name,
                                                 'complete/' + folder + '/images/' + img_name)
                                case "ssli":
                                    nonvalid = False
                                    for line in labels:
                                        match line[0]:
                                            case "6":
                                                nonvalid = True
                                                break
                                            case _:
                                                pass
                                    if not nonvalid:
                                        shutil.copy2(dataset + '/' + folder + '/labels/' + file,
                                                     'complete/' + folder + '/labels/' + file)
                                        img_name = file[:-3] + 'jpg'
                                        shutil.copy2(dataset + '/' + folder + '/images/' + img_name,
                                                     'complete/' + folder + '/images/' + img_name)
                                case "vd":
                                    with open('complete/' + folder + '/labels/' + file, "w") as copy:
                                        nonvalid = False
                                        for line in labels:
                                            match line[0]:
                                                case "0":
                                                    line[0] = "1"
                                                    copy.write(' '.join(line))
                                                case "1":
                                                    line[0] = "2"
                                                    copy.write(' '.join(line))
                                                case "2":
                                                    line[0] = "3"
                                                    copy.write(' '.join(line))
                                                case "3":
                                                    line[0] = "4"
                                                    copy.write(' '.join(line))
                                                case "4":
                                                    nonvalid = True
                                                    break
                                                case "5":
                                                    copy.write(' '.join(line))
                                        if nonvalid:
                                            copy.close()
                                            os.remove('complete/' + folder + '/labels/' + file)
                                        else:
                                            img_name = file[:-3] + 'jpg'
                                            shutil.copy2(dataset + '/' + folder + '/images/' + img_name,
                                                         'complete/' + folder + '/images/' + img_name)
