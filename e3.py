#！usr/bin/env python
import pandas as pd

list_election = []
for i in range(1924,2020,4):
    header = pd.read_csv("president_general_{}.csv".format(i), nrows = 1).dropna(axis = 1, how = "all")

    d = header.iloc[0].to_dict()
    df = pd.read_csv("president_general_{}.csv".format(i), index_col = 0,
               thousands = ",", skiprows = [1])

    df.rename(inplace = True, columns = d) # rename to democrat/republican
    df.dropna(inplace = True, axis = 1)    # drop empty columns
    df["Year"] = i
    list_election.append(df[['Democratic','Republican','Total Votes Cast','Year']])

    df_election = pd.concat(list_election)

    df_election['Republican Share'] = df_election['Republican']/df_election['Total Votes Cast']
    df_election_share = df_election[['Republican Share','Year']]

import matplotlib.pyplot as plt

Accomack_election = df_election_share.loc['Accomack County']
ax = Accomack_election.plot(x ='Year', y ='Republican Share', rot = 70)
ax.set_title("Republican Share in Accomack County in 1924-2016")
ax.set_xlabel("Year")
ax.set_ylabel("Share")

Albemarle_election = df_election_share.loc['Albemarle County']
ax = Albemarle_election.plot(x ='Year', y ='Republican Share', rot = 70)
ax.set_title("Republican Share in Albemarle County in 1924-2016")
ax.set_xlabel("Year")
ax.set_ylabel("Share")

Alexandria_election = df_election_share.loc['Alexandria City']
ax = Alexandria_election.plot(x ='Year', y ='Republican Share', rot = 70)
ax.set_title("Republican Share in Alexandria City in 1924-2016")
ax.set_xlabel("Year")
ax.set_ylabel("Share")

Alleghany_election = df_election_share.loc['Alleghany County']
ax = Alleghany_election.plot(x ='Year', y ='Republican Share', rot = 70)
ax.set_title("Republican Share in Alleghany County in 1924-2016")
ax.set_xlabel("Year")
ax.set_ylabel("Share")

ax.figure.savefig("Accomack.pdf")
ax.figure.savefig("Albemarle.pdf")
ax.figure.savefig("Alexandria.pdf")
ax.figure.savefig("Alleghany.pdf")
