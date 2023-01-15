from typing import List
import pandas as pd

class ExcessiveCancellationsChecker(object):

    def readFile(self, data):
        df =  pd.read_csv(data, sep=",",names=["TimeOfTrade", "CompanyName", "OrderType", "Quantity"])
        return df

    def companies_involved_in_excessive_cancellations(self) -> List[str]:
        """TODO Implement
        Returns the list of companies that are involved in excessive cancelling.
        """
        ec_list = set()
        df = self.readFile('Trades.data')
        # print(df.columns)
        df['TimeOfTrade'] = pd.to_datetime(df['TimeOfTrade'])
        # df['time'] = pd.to_datetime(df['TimeOfTrade']).dt.time
        # print(df.head)
        df['minutes'] = (df.TimeOfTrade - df.loc[0, 'TimeOfTrade']).dt.total_seconds() // 60
        # print(df.head)
        order_df = df[df['OrderType'] == 'D']
        grouped_df1 = order_df.groupby(['CompanyName','minutes']).sum('Quantity').reset_index()
        # print(grouped_df1.head)
        cancelled_df = df[df['OrderType'] == 'F']
        grouped_df2 = cancelled_df.groupby(['CompanyName','minutes']).sum('Quantity').reset_index()
        # print(grouped_df2.head)
        all_companies = df.CompanyName.unique()
        # order_minutes = grouped_df1.minutes.unique()
        # cancelled_minutes = grouped_df2.minutes.unique()

        # print(all_companies)
        grouped_df1['cancel'] = grouped_df2['Quantity']
        grouped_df1['diff'] = grouped_df1['Quantity'] // grouped_df2['Quantity']

        grouped_df1 = grouped_df1[grouped_df1['diff'] < 3]
        final = set(grouped_df1['CompanyName'].to_list())
        ec_list = final

        return list(ec_list)

        



    def total_number_of_well_behaved_companies(self) -> int:
        """TODO Implement
        Returns the total number of companies that are not involved in any excessive cancelling.
        """
        df = self.readFile('Trades.data')
        involved_companies = self.companies_involved_in_excessive_cancellations()

        all_companies = df.CompanyName.unique().tolist()
        # print(all_companies)
        count = 0

        for i in all_companies:
            if i not in involved_companies:
                count += 1

        return count

# _checker = ExcessiveCancellationsChecker()
# # _checker.readFile('Trades.data')
# l = _checker.companies_involved_in_excessive_cancellations()
# print(l)
# c = _checker.total_number_of_well_behaved_companies()
# print(c)

