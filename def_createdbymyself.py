def outlier_IQR(df, col, w=1.5):
    q25 = np.percentile(df[col].values, 25)
    q75 = np.percentile(df[col].values, 75)

    IQR = q75 - q25
    l_est = q25 - (IQR*w)
    h_est = q75 + (IQR*w)

    o_idx = df[col][(df[col]<l_est)|(df[col]>h_est)].index

    return o_idx

def zscr_idx(data, col, tres=3):
    mean = data[col].mean()
    std = data[col].std()
    
    idx = 0
    otrl = []
    otrl_idx = []
    
    for val in data[col]:
        if ((val-mean)/std>tres)|((val-mean)/std<-tres):
            otrl.append(val)
            otrl_idx.append(idx)
        idx+=1
​
    #otrl = [val for val in data[col] if ((val-mean)/std>3)|((val-mean)/std<-3)]
    
    return otrl, otrl_idx
    #zscr_idx[0]=>otrl, zscr_idx[1]=>otrl_idx
    
def del_outlier(df,o_idx):
    df = df.drop(o_idx, axis=0, inplace=True)
  
    return df

def modified_zscr(data, col, k=1.4826):
    med = data[col].median()
    
    #median absolute deviation
    m_a_d = data[col].map(lambda x: np.abs(x-med)).median()
    
    mod_zscr = [data[col].map(lambda x: k/2*(x-med)/m_a_d)]
    return mod_zscr

def binning_IQR(df, col):
    q25 = np.percentile(df[col].values, 25)
    q50 = np.percentile(df[col].values, 50)
    q75 = np.percentile(df[col].values, 75)
    
    belowq25 = df[col][df[col]<q25].values
    q25toq50 = df[col][(df[col]>=q25)&(df[col]<q50)].values
    q50toq75 = df[col][(df[col]<q75)&( df[col]>=q50)].values
    aboveq75 = df[col][df[col]>=q75].values
    
    df[col] = df[col].replace(belowq25,0)
    df[col] = df[col].replace(q25toq50,1)
    df[col] = df[col].replace(q50toq75,2)
    df[col] = df[col].replace(aboveq75,3)

    df[col] = df[col].astype('int64')
    
    return df[col]

