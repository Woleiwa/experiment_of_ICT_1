# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import pandas as pd
import warnings
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":

    warnings.filterwarnings('ignore')
    df = pd.read_csv('telecom_churn.csv')
    i = int(input("Step:"))
    if i == 1:
        print(df.head())
    elif i == 2:
        print(df.shape)
    elif i == 3:
        print(df.columns)
    elif i == 4:
        print(df.info())
    elif i == 5:
        df['Churn'] = df['Churn'].astype('int64')
        print(df.info())
    elif i == 6:
        print(df.describe())
    elif i == 7:
        print(df.describe(include=['object', 'bool']))
    elif i == 8:
        print(df['Churn'].value_counts())
    elif i == 9:
        print(df['Churn'].value_counts(normalize=True))
    elif i == 10:
        print(df.sort_values(by='Total day charge', ascending=False).head())
    elif i == 11:
        print(df.sort_values(by=['Churn', 'Total day charge'],ascending=[True, False]).head())
    elif i == 12:
        print(df['Churn'].mean())
    elif i == 13:
        print(df[df['Churn'] == 1].mean())
    elif i == 14:
        print(df[df['Churn'] == 1]['Total day minutes'].mean())
    elif i == 15:
        print(df[(df['Churn'] == 0) & (df['International plan'] == 'No')]['Total intl minutes'].max())
    elif i == 16:
        print(df.loc[0:5, 'State':'Area code'])
    elif i == 17:
        print(df.iloc[0:5, 0:3])
    elif i == 18:
        print(df[-1:])
    elif i == 19:
        print(df.apply(np.max))
    elif i == 20:
        print(df[df['State'].apply(lambda state: state[0] == 'W')].head())
    
    elif i == 21:
        d = {'No': False, 'Yes': True}
        df['International plan'] = df['International plan'].map(d)
        print(df.head())

    elif i == 22:
        d = {'No': False, 'Yes': True}
        df = df.replace({'Voice mail plan': d})
        print(df.head())

    elif i == 23:
        columns_to_show = ['Total day minutes', 'Total eve minutes','Total night minutes']
        print(df.groupby(['Churn'])[columns_to_show].describe(percentiles=[]))

    elif i == 24:
        columns_to_show = ['Total day minutes', 'Total eve minutes','Total night minutes']
        print(df.groupby(['Churn'])[columns_to_show].agg([np.mean, np.std, np.min, np.max]))

    elif i == 25:
        print(df.pivot_table(['Total day calls', 'Total eve calls', 'Total night calls'], ['Area code'], aggfunc='mean'))

    elif i == 26:
        print(pd.crosstab(df['Churn'], df['International plan']))

    elif i == 27:
        print(pd.crosstab(df['Churn'], df['Voice mail plan'], normalize=True))

    elif i == 28:
        total_calls = df['Total day calls'] + df['Total eve calls'] + df['Total night calls'] + df['Total intl calls']
        # loc 参数是插入 Series 对象后选择的列数
        # 设置为 len(df.columns)以便将计算后的 Total calls 粘贴到最后一列
        df.insert(loc=len(df.columns), column='Total calls', value=total_calls)
        print(df.head())

    elif i == 29:
        df['Total charge'] = df['Total day charge'] + df['Total eve charge'] + df['Total night charge'] + df['Total intl charge']
        print(df.head())

    elif i == 30:
        total_calls = df['Total day calls'] + df['Total eve calls'] + df['Total night calls'] + df['Total intl calls']
        df.insert(loc=len(df.columns), column='Total calls', value=total_calls)
        df['Total charge'] = df['Total day charge'] + df['Total eve charge'] + df['Total night charge'] + df['Total intl charge']
        print(df.head())
        df.drop(['Total charge', 'Total calls'], axis=1, inplace=True)
        print(df.drop([1, 2]).head())

    elif i == 31:
        sns.countplot(x='International plan', hue='Churn', data=df)
        plt.show()

    elif i == 32:
        pd.crosstab(df['Churn'], df['Customer service calls'], margins=True)
        print(sns.countplot(x='Customer service calls', hue='Churn', data=df))
        plt.show()

    elif i == 33:
        df['Many_service_calls'] = (df['Customer service calls'] > 3)
        pd.crosstab(df['Many_service_calls'], df['Churn'], margins=True)
        sns.countplot(x='Many_service_calls', hue='Churn', data=df)
        plt.show()

    elif i == 34:
        df['Many_service_calls'] = (df['Customer service calls'] > 3)
        print(pd.crosstab(df['Many_service_calls'] & df['International plan'], df['Churn']))



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
