import glob, re, fnmatch, os
import collections

def readfile( d, filename, key_index=8, key_count=17, val_index=62, val_count=11, line_len=188, special_index = -1 ):
    with open(filename) as f:
        valid_lines=0
        total_lines=0
        skip_keys=0
        key_index2 = key_index + key_count
        val_index2 = val_index + val_count
        if special_index==-1:
            special_index = key_index2
        check_special=special_index>=0
        for line in f:
            total_lines+=1
            l = len(line)
            if l >= line_len:
                check_key=line[special_index]
                if check_special and (check_key!=' '):
                    skip_keys+=1
                else:
                    valid_lines += 1
                    key = line[key_index:key_index2].strip()
                    val = line[val_index:val_index2].strip()
                    d[key] = val
    print("{0}: valid: {1}/{2} skip_keys:{3}".format(filename,valid_lines,total_lines,skip_keys))

def readoutfile( d, filename):
    with open(filename) as f:
        total_lines=0
        for line in f:
            line=line.strip().rstrip('\n')
            if line=='':
                continue
            total_lines+=1
            kv=re.split(r'\t+', line)
            key = kv[0]
            val = kv[1]
            d[key] = val
    print("{0}: base lines: {1}".format(filename,total_lines))

def writefile(d, filename):
    od = collections.OrderedDict(sorted(d.items()))
    count = len(od)
    if count>0:
        text_file = open(filename, "w")
        for k, v in od.iteritems():
            if float(v)!=0:
                s='{0}\t{1}\n'.format(k,v)
                text_file.write(s)
        print("Writing: {0}: {1} lines".format(filename,count))
        text_file.close()
    else:
        print("No items found!")

def read_write(dir, base_file='base.txt', in_pattern='*.NEW', outfile='NEW_PRICE_LIST.txt'):
    d = {}
    #dir=os.getcwd()
    if dir!='':
        os.chdir(dir)
    if base_file!='':
        s = os.path.join(dir,base_file)
        if os.path.isfile(s):
            readoutfile(d, s)
    #for filename in re.compile(fnmatch.translate(in_pattern), re.IGNORECASE):
    for filename in sorted(glob.glob(in_pattern)):
        if filename==base_file:
            continue
        readfile(d, os.path.join(dir, filename))
    writefile(d, os.path.join(dir, outfile))
