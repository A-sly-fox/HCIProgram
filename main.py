import numpy as np
import func
import data

if __name__ == "__main__":
    fpo = open("Output.txt", "w")
    func.GenMatrixP()
    P = func.GetMatrix("Matrix_P.txt")
    R = func.GetMatrix("Matrix_R.txt")

    cycle_num = 0
    w_list = []             # record min_w

    while cycle_num < data.MIN_CYCLE_NUM or func.JudgeOpt(w_list):
        min_w, min_f = func.Traversing(P, R)
        cycle_num += 1
        print("{}\t{}\t{}".format(cycle_num, min_w, min_f))
        fpo.write("No.{}\n{}\n{}\n\n".format(cycle_num, min_f, min_w))

        fpo.write("\t{}\t{}\t{}\n".format(chr(min_f[0]+65),chr(min_f[1]+65),chr(min_f[2]+65)))
        fpo.write("{}\t{}\t{}\t{}\t{}\n".format(chr(min_f[3]+65),chr(min_f[4]+65),chr(min_f[5]+65),chr(min_f[6]+65),chr(min_f[7]+65)))
        fpo.write("\t{}\t{}\t{}\t{}\n".format(chr(min_f[8]+65),chr(min_f[9]+65),chr(min_f[10]+65),chr(min_f[11]+65)))
        fpo.write("\t{}\t{}\t{}\t{}\n".format(chr(min_f[12]+65),chr(min_f[13]+65),chr(min_f[14]+65),chr(min_f[15]+65)))
        fpo.write("\t{}\t{}\t{}\t{}\n".format(chr(min_f[16]+65),chr(min_f[17]+65),chr(min_f[18]+65),chr(min_f[19]+65)))
        fpo.write("\t\t{}\t{}\t{}\n".format(chr(min_f[20]+65),chr(min_f[21]+65),chr(min_f[22]+65)))
        fpo.write("\t\t{}\t{}\t{}\n".format(chr(min_f[23]+65),chr(min_f[24]+65),chr(min_f[25]+65)))

        w_list.append(min_w)    # for JudgeOpt
        data.f_init = min_f[:]  # use f_min as the init f of next cycle

    fpo.close()