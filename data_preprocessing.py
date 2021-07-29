import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns


def prepare_data():
    data_df = pd.read_csv('Dataset/data.csv')
    data_df = data_df.drop(['Thời gian'], axis=1)

    data_df['danh_gia'] = data_df['danh_gia'].replace("Tốt", 0)
    data_df['danh_gia'] = data_df['danh_gia'].replace("Đạt", 1)
    data_df['danh_gia'] = data_df['danh_gia'].replace("Kém", 2)

    data_df['thoi_tiet'] = data_df['thoi_tiet'].replace("Nắng", 0)
    data_df['thoi_tiet'] = data_df['thoi_tiet'].replace("Mưa", 1)

    raw_X, raw_y = data_df.loc[:, data_df.columns != 'danh_gia'], data_df['danh_gia']

    return raw_X, raw_y


def normalize_data():
    raw_X, raw_y = prepare_data()
    scaler = StandardScaler()
    scaler = scaler.fit(raw_X)
    raw_X_std = scaler.transform(raw_X)
    X_train, X_test, y_train, y_test = train_test_split(raw_X_std, raw_y, test_size=0.33, random_state=42)
    return X_train, X_test, y_train, y_test


def normalize_data_predict(x):
    raw_X, raw_y = prepare_data()
    scaler = StandardScaler()
    scaler = scaler.fit(raw_X)
    x_std = scaler.transform([x])
    return x_std


def create_pp_data_pics():
    data_df = pd.read_csv('Dataset/data.csv')
    data_df = data_df.drop(['Thời gian'], axis=1)
    fig = plt.figure(figsize=(20, 13))
    gs = fig.add_gridspec(3, 3)
    gs.update(wspace=0.4, hspace=0.4)
    # adding figures
    ax0 = fig.add_subplot(gs[0, 0])
    background_color = '#f6f5f7'
    fig.patch.set_facecolor(background_color)
    # https://www.geeksforgeeks.org/kde-plot-visualization-with-pandas-and-seaborn/
    sns.kdeplot(ax=ax0, x=data_df.loc[data_df['danh_gia'] == 'Tốt']['cong_suat_phat_olt'], color='crimson', label='Tốt',
                shade=True)
    sns.kdeplot(ax=ax0, x=data_df.loc[data_df['danh_gia'] == 'Đạt']['cong_suat_phat_olt'], color='coral', label='Đạt',
                shade=True)
    sns.kdeplot(ax=ax0, x=data_df.loc[data_df['danh_gia'] == 'Kém']['cong_suat_phat_olt'], color='red', label='Kém',
                shade=True)
    ax0.legend(loc='upper left')
    fig.savefig('static/img/cong_suat_phat_olt.png')

    fig = plt.figure(figsize=(20, 13))
    gs = fig.add_gridspec(3, 3)
    gs.update(wspace=0.4, hspace=0.4)
    # adding figures
    ax0 = fig.add_subplot(gs[0, 0])
    background_color = '#f6f5f7'
    fig.patch.set_facecolor(background_color)
    # https://www.geeksforgeeks.org/kde-plot-visualization-with-pandas-and-seaborn/
    sns.kdeplot(ax=ax0, x=data_df.loc[data_df['danh_gia'] == 'Tốt']['cong_suat_thua_olt'], color='crimson', label='Tốt',
                shade=True)
    sns.kdeplot(ax=ax0, x=data_df.loc[data_df['danh_gia'] == 'Đạt']['cong_suat_thua_olt'], color='coral', label='Đạt',
                shade=True)
    sns.kdeplot(ax=ax0, x=data_df.loc[data_df['danh_gia'] == 'Kém']['cong_suat_thua_olt'], color='red', label='Kém',
                shade=True)
    ax0.legend(loc='upper left')
    fig.savefig('static/img/cong_suat_thu_olt.png')

    fig = plt.figure(figsize=(20, 13))
    gs = fig.add_gridspec(3, 3)
    gs.update(wspace=0.4, hspace=0.4)
    # adding figures
    ax0 = fig.add_subplot(gs[0, 0])
    background_color = '#f6f5f7'
    fig.patch.set_facecolor(background_color)
    # https://www.geeksforgeeks.org/kde-plot-visualization-with-pandas-and-seaborn/
    sns.kdeplot(ax=ax0, x=data_df.loc[data_df['danh_gia'] == 'Tốt']['cong_suat_phat_thiet_bi_dau_cuoi'],
                color='crimson', label='Tốt', shade=True)
    sns.kdeplot(ax=ax0, x=data_df.loc[data_df['danh_gia'] == 'Đạt']['cong_suat_phat_thiet_bi_dau_cuoi'], color='coral',
                label='Đạt', shade=True)
    sns.kdeplot(ax=ax0, x=data_df.loc[data_df['danh_gia'] == 'Kém']['cong_suat_phat_thiet_bi_dau_cuoi'], color='red',
                label='Kém', shade=True)
    ax0.legend(loc='upper left')
    fig.savefig('static/img/cong_suat_phat_thiet_bi_dau_cuoi.png')

    fig = plt.figure(figsize=(20, 13))
    gs = fig.add_gridspec(3, 3)
    gs.update(wspace=0.4, hspace=0.4)
    # adding figures
    ax0 = fig.add_subplot(gs[0, 0])
    background_color = '#f6f5f7'
    fig.patch.set_facecolor(background_color)
    # https://www.geeksforgeeks.org/kde-plot-visualization-with-pandas-and-seaborn/
    sns.kdeplot(ax=ax0, x=data_df.loc[data_df['danh_gia'] == 'Tốt']['cong_suat_thu_thiet_bi_dau_cuoi'], color='crimson',
                label='Tốt', shade=True)
    sns.kdeplot(ax=ax0, x=data_df.loc[data_df['danh_gia'] == 'Đạt']['cong_suat_thu_thiet_bi_dau_cuoi'], color='coral',
                label='Đạt', shade=True)
    sns.kdeplot(ax=ax0, x=data_df.loc[data_df['danh_gia'] == 'Kém']['cong_suat_thu_thiet_bi_dau_cuoi'], color='red',
                label='Kém', shade=True)
    ax0.legend(loc='upper left')
    fig.savefig('static/img/cong_suat_thu_thiet_bi_dau_cuoi.png')

    fig = plt.figure(figsize=(20, 13))
    gs = fig.add_gridspec(3, 3)
    gs.update(wspace=0.4, hspace=0.4)
    # adding figures
    ax0 = fig.add_subplot(gs[0, 0])
    background_color = '#f6f5f7'
    fig.patch.set_facecolor(background_color)
    # https://www.geeksforgeeks.org/kde-plot-visualization-with-pandas-and-seaborn/
    sns.kdeplot(ax=ax0, x=data_df.loc[data_df['danh_gia'] == 'Tốt']['suy_hao_download'], color='crimson', label='Tốt',
                shade=True)
    sns.kdeplot(ax=ax0, x=data_df.loc[data_df['danh_gia'] == 'Đạt']['suy_hao_download'], color='coral', label='Đạt',
                shade=True)
    sns.kdeplot(ax=ax0, x=data_df.loc[data_df['danh_gia'] == 'Kém']['suy_hao_download'], color='red', label='Kém',
                shade=True)
    ax0.legend(loc='upper left')
    fig.savefig('static/img/suy_hao_download.png')

    fig = plt.figure(figsize=(20, 13))
    gs = fig.add_gridspec(3, 3)
    gs.update(wspace=0.4, hspace=0.4)
    # adding figures
    ax0 = fig.add_subplot(gs[0, 0])
    background_color = '#f6f5f7'
    fig.patch.set_facecolor(background_color)
    # https://www.geeksforgeeks.org/kde-plot-visualization-with-pandas-and-seaborn/
    sns.kdeplot(ax=ax0, x=data_df.loc[data_df['danh_gia'] == 'Tốt']['suy_hao_upload'], color='crimson', label='Tốt',
                shade=True)
    sns.kdeplot(ax=ax0, x=data_df.loc[data_df['danh_gia'] == 'Đạt']['suy_hao_upload'], color='coral', label='Đạt',
                shade=True)
    sns.kdeplot(ax=ax0, x=data_df.loc[data_df['danh_gia'] == 'Kém']['suy_hao_upload'], color='red', label='Kém',
                shade=True)
    ax0.legend(loc='upper left')
    fig.savefig('static/img/suy_hao_upload.png')

    fig = plt.figure(figsize=(20, 13))
    gs = fig.add_gridspec(3, 3)
    gs.update(wspace=0.4, hspace=0.4)
    # adding figures
    ax0 = fig.add_subplot(gs[0, 0])
    background_color = '#f6f5f7'
    fig.patch.set_facecolor(background_color)
    # https://www.geeksforgeeks.org/kde-plot-visualization-with-pandas-and-seaborn/
    sns.kdeplot(ax=ax0, x=data_df.loc[data_df['danh_gia'] == 'Tốt']['khoang_cach_thue_bao'], color='crimson',
                label='Tốt', shade=True)
    sns.kdeplot(ax=ax0, x=data_df.loc[data_df['danh_gia'] == 'Đạt']['khoang_cach_thue_bao'], color='coral', label='Đạt',
                shade=True)
    sns.kdeplot(ax=ax0, x=data_df.loc[data_df['danh_gia'] == 'Kém']['khoang_cach_thue_bao'], color='red', label='Kém',
                shade=True)
    ax0.legend(loc='upper left')
    fig.savefig('static/img/khoang_cach_thue_bao.png')

    class_occur = data_df['danh_gia'].value_counts()
    class_names = ['0', '1', '2']
    fig, ax = plt.subplots()
    ax.pie(class_occur, labels=class_names, autopct='%1.2f%%',
           shadow=True, startangle=0, counterclock=False)
    ax.axis('equal')
    ax.set_title('Class distribution')
    plt.savefig('static/img/phan_phoi_class.png')
