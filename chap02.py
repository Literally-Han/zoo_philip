{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "124a181a-7e06-4428-bfe7-00c6b727aba6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'%.3f'"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "%precision 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "517a64bf-960f-40dd-beec-a02a0a57a0dd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>english</th>\n",
       "      <th>mathematics</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>student number</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>42</td>\n",
       "      <td>65</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>69</td>\n",
       "      <td>80</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>56</td>\n",
       "      <td>63</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>41</td>\n",
       "      <td>63</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>57</td>\n",
       "      <td>76</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                english  mathematics\n",
       "student number                      \n",
       "1                    42           65\n",
       "2                    69           80\n",
       "3                    56           63\n",
       "4                    41           63\n",
       "5                    57           76"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df=pd.read_csv(r\"C:\\Users\\한민종\\Desktop\\통계분석\\python_stat_sample-master\\data\\ch2_scores_em.csv\",\n",
    "               index_col='student number')\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "d59cbcd8-1cc4-42e8-9e1b-7c353789ace9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([42, 69, 56, 41, 57, 48, 65, 49, 65, 58])"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "scores=np.array(df['english'])[:10]\n",
    "scores"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "a2ef2df8-6098-47d7-bfae-ee329726dfe9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>scores</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>student</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>A</th>\n",
       "      <td>42</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>B</th>\n",
       "      <td>69</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>C</th>\n",
       "      <td>56</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>D</th>\n",
       "      <td>41</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>E</th>\n",
       "      <td>57</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>F</th>\n",
       "      <td>48</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>G</th>\n",
       "      <td>65</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>H</th>\n",
       "      <td>49</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>I</th>\n",
       "      <td>65</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>J</th>\n",
       "      <td>58</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         scores\n",
       "student        \n",
       "A            42\n",
       "B            69\n",
       "C            56\n",
       "D            41\n",
       "E            57\n",
       "F            48\n",
       "G            65\n",
       "H            49\n",
       "I            65\n",
       "J            58"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "scores_df=pd.DataFrame({'scores':scores},\n",
    "                       index=pd.Index(['A','B','C','D','E','F','G','H','I','J'], \n",
    "                        name='student'))\n",
    "scores_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "f2187a6c-5482-48d9-971b-761108c2d6c6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "55.000"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sum(scores)/len(scores)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "dd3a652a-2b2b-45a1-8251-958ba0850b2f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "55.000"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.mean(scores)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "715faff4-b461-48d7-897c-41f0b872b206",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "scores    55.0\n",
       "dtype: float64"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "scores_df.mean()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "2c651016-538c-4fdd-a82a-17d0afed61a7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([41, 42, 48, 49, 56, 57, 58, 65, 65, 69])"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sorted_scores=np.sort(scores)\n",
    "sorted_scores"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "74fe758e-5db1-499b-8ecc-0bad0a37b567",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "56.500"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "n=len(sorted_scores)\n",
    "if n % 2== 0:\n",
    "    m0=sorted_scores[n//2-1]\n",
    "    m1=sorted_scores[n//2]\n",
    "    median=(m0+m1)/2\n",
    "else:\n",
    "    median=sorted_scores[(n+1)//2-1]\n",
    "median"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "d0bd37db-e7f6-4303-a7e8-65bcd48f28af",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "56.500"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.median(scores)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "b8e5a857-0202-4671-a45a-9e8f54f840a2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "scores    56.5\n",
       "dtype: float64"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "scores_df.median()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "506143ac-5ec7-4310-a45b-95db3b9bea9f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    1\n",
       "dtype: int64"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.Series([1,1,1,2,2,3]).mode()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "17745560-430a-4871-9e73-f48bad811941",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    1\n",
       "1    2\n",
       "2    3\n",
       "3    4\n",
       "4    5\n",
       "dtype: int64"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.Series([1,2,3,4,5]).mode()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "e8a9fdc5-6b7d-4c9f-a703-ed4c0050236d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([-13.,  14.,   1., -14.,   2.,  -7.,  10.,  -6.,  10.,   3.])"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mean=np.mean(scores)\n",
    "deviation=scores-mean\n",
    "deviation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "48923dba-97b1-43df-ab1d-a0e891cf6ecc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([-5.,  5.,  3., -1., -4.,  1.,  2., -2., -3.,  4.])"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "another_scores=[50,60,58,54,51,56,57,53,52,59]\n",
    "another_mean=np.mean(another_scores)\n",
    "another_deviation=another_scores-another_mean\n",
    "another_deviation\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "f671848a-41a3-4f35-aac5-49db0951d118",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'%.3f'"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "%precision 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "f770a818-beae-4c38-9c8c-2fd44f0fa886",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.000"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.mean(deviation)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "ffa6691a-bb0a-4e5b-a333-b42545c8408d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.000"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.mean(another_deviation)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "4e7925fc-0f13-469d-8024-0ff5999a5a78",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>scores</th>\n",
       "      <th>deviation</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>student</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>A</th>\n",
       "      <td>42</td>\n",
       "      <td>-13.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>B</th>\n",
       "      <td>69</td>\n",
       "      <td>14.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>C</th>\n",
       "      <td>56</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>D</th>\n",
       "      <td>41</td>\n",
       "      <td>-14.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>E</th>\n",
       "      <td>57</td>\n",
       "      <td>2.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>F</th>\n",
       "      <td>48</td>\n",
       "      <td>-7.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>G</th>\n",
       "      <td>65</td>\n",
       "      <td>10.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>H</th>\n",
       "      <td>49</td>\n",
       "      <td>-6.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>I</th>\n",
       "      <td>65</td>\n",
       "      <td>10.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>J</th>\n",
       "      <td>58</td>\n",
       "      <td>3.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         scores  deviation\n",
       "student                   \n",
       "A            42      -13.0\n",
       "B            69       14.0\n",
       "C            56        1.0\n",
       "D            41      -14.0\n",
       "E            57        2.0\n",
       "F            48       -7.0\n",
       "G            65       10.0\n",
       "H            49       -6.0\n",
       "I            65       10.0\n",
       "J            58        3.0"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "summary_df=scores_df.copy()\n",
    "summary_df['deviation']=deviation\n",
    "summary_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "be45d04d-0ef1-45b2-9d8e-04e1726f3ec4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "86.000"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.mean(deviation**2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "030c0848-fc66-4e52-8ae4-cd204e914ff1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "86.000"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.var(scores)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "89042b19-8d8f-487c-a0e2-061d2fc10bbf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "scores    95.555556\n",
       "dtype: float64"
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "scores_df.var()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "96ea5e44-7eab-4bea-906f-daab24c9ea2f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>scores</th>\n",
       "      <th>deviation</th>\n",
       "      <th>square of deviation</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>student</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>A</th>\n",
       "      <td>42</td>\n",
       "      <td>-13.0</td>\n",
       "      <td>169.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>B</th>\n",
       "      <td>69</td>\n",
       "      <td>14.0</td>\n",
       "      <td>196.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>C</th>\n",
       "      <td>56</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>D</th>\n",
       "      <td>41</td>\n",
       "      <td>-14.0</td>\n",
       "      <td>196.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>E</th>\n",
       "      <td>57</td>\n",
       "      <td>2.0</td>\n",
       "      <td>4.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>F</th>\n",
       "      <td>48</td>\n",
       "      <td>-7.0</td>\n",
       "      <td>49.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>G</th>\n",
       "      <td>65</td>\n",
       "      <td>10.0</td>\n",
       "      <td>100.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>H</th>\n",
       "      <td>49</td>\n",
       "      <td>-6.0</td>\n",
       "      <td>36.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>I</th>\n",
       "      <td>65</td>\n",
       "      <td>10.0</td>\n",
       "      <td>100.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>J</th>\n",
       "      <td>58</td>\n",
       "      <td>3.0</td>\n",
       "      <td>9.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         scores  deviation  square of deviation\n",
       "student                                        \n",
       "A            42      -13.0                169.0\n",
       "B            69       14.0                196.0\n",
       "C            56        1.0                  1.0\n",
       "D            41      -14.0                196.0\n",
       "E            57        2.0                  4.0\n",
       "F            48       -7.0                 49.0\n",
       "G            65       10.0                100.0\n",
       "H            49       -6.0                 36.0\n",
       "I            65       10.0                100.0\n",
       "J            58        3.0                  9.0"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "summary_df['square of deviation']=np.square(deviation)\n",
    "summary_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "c7362446-6dac-4654-9116-9f8fc2056a25",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9.274"
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.sqrt(np.var(scores,ddof=0))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "69294f65-0a54-4380-a096-ccc2f77cacda",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9.274"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.std(scores,ddof=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "5d8e6eb2-8cc0-4a10-8d9a-bf27dd7610e7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.int64(28)"
      ]
     },
     "execution_count": 82,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.max(scores)-np.min(scores)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "448c1d0d-2874-4332-b4da-91f66f9cf9db",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "15.000"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "scores_Q1=np.percentile(scores,25)\n",
    "scores_Q3=np.percentile(scores,75)\n",
    "scores_IQR=scores_Q3-scores_Q1\n",
    "scores_IQR"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "2b062994-a6e6-46ff-be7a-50ab06011c1e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    10.000000\n",
       "mean     55.000000\n",
       "std       9.775252\n",
       "min      41.000000\n",
       "25%      48.250000\n",
       "50%      56.500000\n",
       "75%      63.250000\n",
       "max      69.000000\n",
       "dtype: float64"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.Series(scores).describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "45b1d66f-4372-4fb6-b3d7-9e4124005f5f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([-1.402,  1.51 ,  0.108, -1.51 ,  0.216, -0.755,  1.078, -0.647,\n",
       "        1.078,  0.323])"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "z=(scores-np.mean(scores))/np.std(scores)\n",
    "z"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "ab8d3191-a1ae-4f88-914b-7461256bde66",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(-0.000, 1.000)"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.mean(z), np.std(z,ddof=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "302761cb-1554-483a-ab3b-87b4c714954b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([35.982, 65.097, 51.078, 34.903, 52.157, 42.452, 60.783, 43.53 ,\n",
       "       60.783, 53.235])"
      ]
     },
     "execution_count": 87,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "z=50+10*(scores-np.mean(scores))/np.std(scores)\n",
    "z\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "7ed90052-0e1f-4f55-8812-20903bca3ccc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>scores</th>\n",
       "      <th>deviation vallue</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>student</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>A</th>\n",
       "      <td>42</td>\n",
       "      <td>35.981739</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>B</th>\n",
       "      <td>69</td>\n",
       "      <td>65.096588</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>C</th>\n",
       "      <td>56</td>\n",
       "      <td>51.078328</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>D</th>\n",
       "      <td>41</td>\n",
       "      <td>34.903412</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>E</th>\n",
       "      <td>57</td>\n",
       "      <td>52.156655</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>F</th>\n",
       "      <td>48</td>\n",
       "      <td>42.451706</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>G</th>\n",
       "      <td>65</td>\n",
       "      <td>60.783277</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>H</th>\n",
       "      <td>49</td>\n",
       "      <td>43.530034</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>I</th>\n",
       "      <td>65</td>\n",
       "      <td>60.783277</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>J</th>\n",
       "      <td>58</td>\n",
       "      <td>53.234983</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         scores  deviation vallue\n",
       "student                          \n",
       "A            42         35.981739\n",
       "B            69         65.096588\n",
       "C            56         51.078328\n",
       "D            41         34.903412\n",
       "E            57         52.156655\n",
       "F            48         42.451706\n",
       "G            65         60.783277\n",
       "H            49         43.530034\n",
       "I            65         60.783277\n",
       "J            58         53.234983"
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "scores_df['deviation vallue']=z\n",
    "scores_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "8a492093-141d-414f-913b-304d55fffd3a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    50.000000\n",
       "mean     58.380000\n",
       "std       9.799813\n",
       "min      37.000000\n",
       "25%      54.000000\n",
       "50%      57.500000\n",
       "75%      65.000000\n",
       "max      79.000000\n",
       "dtype: float64"
      ]
     },
     "execution_count": 89,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "english_scores=np.array(df['english'])\n",
    "pd.Series(english_scores).describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "343df639-bdbd-44e8-8467-45360b9cd215",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 0,  0,  0,  2,  8, 16, 18,  6,  0,  0])"
      ]
     },
     "execution_count": 90,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "freq,_=np.histogram(english_scores, bins=10, range=(0,100))\n",
    "freq"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "416acaa4-413c-4985-9316-85571aaab623",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>frequency</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>class</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0~10</th>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10~20</th>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20~30</th>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>30~40</th>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>40~50</th>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50~60</th>\n",
       "      <td>16</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>60~70</th>\n",
       "      <td>18</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>70~80</th>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>80~90</th>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>90~100</th>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        frequency\n",
       "class            \n",
       "0~10            0\n",
       "10~20           0\n",
       "20~30           0\n",
       "30~40           2\n",
       "40~50           8\n",
       "50~60          16\n",
       "60~70          18\n",
       "70~80           6\n",
       "80~90           0\n",
       "90~100          0"
      ]
     },
     "execution_count": 93,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "freq_class=[f'{i}~{i+10}' for i in range(0,100,10)]\n",
    "freq_dist_df=pd.DataFrame({'frequency':freq}, \n",
    "                          index=pd.Index(freq_class,\n",
    "                                         name='class'))\n",
    "freq_dist_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "7838b3d4-5eca-4ea1-b834-dd0c53d5b60c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "6\n"
     ]
    }
   ],
   "source": [
    "for a in range(7):\n",
    "    print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "329b8e0c-6773-4203-a914-e24517089c80",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "9\n",
      "8\n",
      "7\n",
      "6\n"
     ]
    }
   ],
   "source": [
    "for a in range(10,5,-1):\n",
    "    print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "9a28cf32-25a5-43e4-af85-ee804c9025a3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20\n",
      "22\n",
      "24\n",
      "26\n",
      "28\n",
      "30\n"
     ]
    }
   ],
   "source": [
    "for a in range(20,31,2):\n",
    "    print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "bbf88b4a-2ef9-4e3b-8109-9b01e5bb7d3d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "45\n"
     ]
    }
   ],
   "source": [
    "total=0\n",
    "for i in range(1,10):\n",
    "    total=total+i\n",
    "print(total)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "id": "63c9447f-7ae3-4a0f-8776-4f296e36fad8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "25\n"
     ]
    }
   ],
   "source": [
    "total=0\n",
    "for i  in range(1,10,2):\n",
    "    total=total + i\n",
    "print(total)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "id": "3e235c61-575a-48b1-9c07-f594c5652037",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[5, 15, 25, 35, 45, 55, 65, 75, 85, 95]"
      ]
     },
     "execution_count": 103,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "class_value=[(i+(i+10))//2 for i in range(0,100,10)]\n",
    "class_value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "id": "7b7c8fa1-a9f1-4e75-92b1-9778373b7a79",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0.  , 0.  , 0.  , 0.04, 0.16, 0.32, 0.36, 0.12, 0.  , 0.  ])"
      ]
     },
     "execution_count": 104,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rel_freq=freq/freq.sum()\n",
    "rel_freq"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "id": "58fd1008-02f5-45fa-b1a0-d53494a6d794",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0.  , 0.  , 0.  , 0.04, 0.2 , 0.52, 0.88, 1.  , 1.  , 1.  ])"
      ]
     },
     "execution_count": 106,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cum_rel_freq=np.cumsum(rel_freq)\n",
    "cum_rel_freq"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "id": "1f22f7ef-8dcf-47ba-a5a2-44fbcbc9f213",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>class value</th>\n",
       "      <th>frequency</th>\n",
       "      <th>relative frequency</th>\n",
       "      <th>cumulative relative frequency</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>class</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0~10</th>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10~20</th>\n",
       "      <td>15</td>\n",
       "      <td>0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20~30</th>\n",
       "      <td>25</td>\n",
       "      <td>0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>30~40</th>\n",
       "      <td>35</td>\n",
       "      <td>2</td>\n",
       "      <td>0.04</td>\n",
       "      <td>0.04</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>40~50</th>\n",
       "      <td>45</td>\n",
       "      <td>8</td>\n",
       "      <td>0.16</td>\n",
       "      <td>0.20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50~60</th>\n",
       "      <td>55</td>\n",
       "      <td>16</td>\n",
       "      <td>0.32</td>\n",
       "      <td>0.52</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>60~70</th>\n",
       "      <td>65</td>\n",
       "      <td>18</td>\n",
       "      <td>0.36</td>\n",
       "      <td>0.88</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>70~80</th>\n",
       "      <td>75</td>\n",
       "      <td>6</td>\n",
       "      <td>0.12</td>\n",
       "      <td>1.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>80~90</th>\n",
       "      <td>85</td>\n",
       "      <td>0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>1.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>90~100</th>\n",
       "      <td>95</td>\n",
       "      <td>0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>1.00</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        class value  frequency  relative frequency  \\\n",
       "class                                                \n",
       "0~10              5          0                0.00   \n",
       "10~20            15          0                0.00   \n",
       "20~30            25          0                0.00   \n",
       "30~40            35          2                0.04   \n",
       "40~50            45          8                0.16   \n",
       "50~60            55         16                0.32   \n",
       "60~70            65         18                0.36   \n",
       "70~80            75          6                0.12   \n",
       "80~90            85          0                0.00   \n",
       "90~100           95          0                0.00   \n",
       "\n",
       "        cumulative relative frequency  \n",
       "class                                  \n",
       "0~10                             0.00  \n",
       "10~20                            0.00  \n",
       "20~30                            0.00  \n",
       "30~40                            0.04  \n",
       "40~50                            0.20  \n",
       "50~60                            0.52  \n",
       "60~70                            0.88  \n",
       "70~80                            1.00  \n",
       "80~90                            1.00  \n",
       "90~100                           1.00  "
      ]
     },
     "execution_count": 108,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "freq_dist_df['class value']=class_value\n",
    "freq_dist_df['relative frequency']=rel_freq\n",
    "freq_dist_df['cumulative relative frequency']=cum_rel_freq\n",
    "freq_dist_df=freq_dist_df[['class value','frequency',\n",
    "                           'relative frequency', 'cumulative relative frequency']]\n",
    "freq_dist_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "id": "84b3b7fb-9a18-4e4a-ac12-011dbf12e7c8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.int64(65)"
      ]
     },
     "execution_count": 110,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "freq_dist_df.loc[freq_dist_df['frequency'].idxmax(),'class value']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "id": "7b73d1f7-c905-47dd-b905-73af8b92abe3",
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "id": "b97070ff-c829-4053-9a9f-a7549e5ff3b9",
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "id": "178f4b29-ba0a-4723-a6bf-29fb81a9fb8b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA0UAAAH/CAYAAACYSXaPAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAIKlJREFUeJzt3X9s1fW9+PFXobTV7baLMGsR7OquTjYydmkDo65ZdFoDhhtuttDFxaoXkzXbLhd63Qay6CBLmrubmXudglsEzRL0Nvgr/tE5mps7fgg3GU27LEK2RZiF2UpasxZ1KwKf+4df+r1di3IObbG8H4/k/HHevN/nvI952/Dkc05PQZZlWQAAACRq2sXeAAAAwMUkigAAgKSJIgAAIGmiCAAASJooAgAAkiaKAACApIkiAAAgaaIIAABImigCAACSJooAAICk5RxFu3fvjuXLl8fs2bOjoKAgXnjhhQ9cs2vXrqiuro6SkpK49tpr47HHHstnrwAAAOMu5yh6++23Y8GCBfHII4+c1/wjR47EsmXLoq6uLjo7O+P++++P1atXx7PPPpvzZgEAAMZbQZZlWd6LCwri+eefjxUrVpxzzne/+9148cUX49ChQ8NjTU1N8etf/zr279+f71MDAACMi8KJfoL9+/dHfX39iLHbbrsttm7dGu+++27MmDFj1JqhoaEYGhoavn/mzJl48803Y+bMmVFQUDDRWwYAAD6ksiyLEydOxOzZs2PatPH5FQkTHkW9vb1RXl4+Yqy8vDxOnToVfX19UVFRMWpNS0tLbNy4caK3BgAATFFHjx6NOXPmjMtjTXgURcSoqztn37F3rqs+69evj+bm5uH7AwMDcc0118TRo0ejtLR04jYKAAB8qA0ODsbcuXPjb/7mb8btMSc8iq666qro7e0dMXb8+PEoLCyMmTNnjrmmuLg4iouLR42XlpaKIgAAYFw/VjPh31O0ZMmSaG9vHzG2c+fOqKmpGfPzRAAAAJMp5yh66623oqurK7q6uiLivV+53dXVFd3d3RHx3lvfGhsbh+c3NTXFa6+9Fs3NzXHo0KHYtm1bbN26Ne67777xeQUAAAAXIOe3zx04cCBuuumm4ftnP/tz1113xZNPPhk9PT3DgRQRUVVVFW1tbbF27dp49NFHY/bs2fHwww/Hl7/85XHYPgAAwIW5oO8pmiyDg4NRVlYWAwMDPlMEAAAJm4g2mPDPFAEAAHyYiSIAACBpoggAAEiaKAIAAJImigAAgKSJIgAAIGmiCAAASJooAgAAkiaKAACApIkiAAAgaaIIAABImigCAACSJooAAICkiSIAACBpoggAAEiaKAIAAJImigAAgKSJIgAAIGmiCAAASJooAgAAkiaKAACApIkiAAAgaaIIAABImigCAACSJooAAICkiSIAACBpoggAAEiaKAIAAJImigAAgKSJIgAAIGmiCAAASJooAgAAkiaKAACApIkiAAAgaaIIAABImigCAACSJooAAICkiSIAACBpoggAAEiaKAIAAJImigAAgKSJIgAAIGmiCAAASJooAgAAkiaKAACApIkiAAAgaaIIAABImigCAACSJooAAICkiSIAACBpoggAAEiaKAIAAJImigAAgKSJIgAAIGmiCAAASJooAgAAkiaKAACApIkiAAAgaaIIAABImigCAACSJooAAICkiSIAACBpoggAAEiaKAIAAJImigAAgKSJIgAAIGmiCAAASJooAgAAkiaKAACApIkiAAAgaaIIAABImigCAACSJooAAICkiSIAACBpoggAAEiaKAIAAJImigAAgKSJIgAAIGmiCAAASJooAgAAkiaKAACApOUVRZs3b46qqqooKSmJ6urq2LNnz/vO3759eyxYsCAuv/zyqKioiHvuuSf6+/vz2jAAAMB4yjmKWltbY82aNbFhw4bo7OyMurq6WLp0aXR3d485f+/evdHY2BirVq2KV155JXbs2BG/+tWv4t57773gzQMAAFyonKPooYceilWrVsW9994b8+bNi3//93+PuXPnxpYtW8ac/z//8z/xiU98IlavXh1VVVXxhS98Ib7+9a/HgQMHLnjzAAAAFyqnKDp58mR0dHREfX39iPH6+vrYt2/fmGtqa2vj2LFj0dbWFlmWxRtvvBHPPPNM3H777fnvGgAAYJzkFEV9fX1x+vTpKC8vHzFeXl4evb29Y66pra2N7du3R0NDQxQVFcVVV10VH/vYx+LHP/7xOZ9naGgoBgcHR9wAAAAmQl6/aKGgoGDE/SzLRo2ddfDgwVi9enU88MAD0dHRES+99FIcOXIkmpqazvn4LS0tUVZWNnybO3duPtsEAAD4QAVZlmXnO/nkyZNx+eWXx44dO+If/uEfhsf/+Z//Obq6umLXrl2j1tx5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QNJEEQAAkDRRBAAAJE0UAQAASRNFAABA0kQRAACQNFEEAAAkTRQBAABJE0UAAEDSRBEAAJA0UQQAACRNFAEAAEkTRQAAQNJEEQAAkDRRBAAAJE0UAQAASRNFAABA0kQRAACQNFEEAAAkTRQBAABJE0UAAEDSRBEAAJA0UQQAACQtryjavHlzVFVVRUlJSVRXV8eePXvOa93LL78chYWF8bnPfS6fpwUAABh3OUdRa2trrFmzJjZs2BCdnZ1RV1cXS5cuje7u7vddNzAwEI2NjfGlL30p780CAACMt4Isy7JcFixevDgWLlwYW7ZsGR6bN29erFixIlpaWs657qtf/Wpcd911MX369HjhhReiq6vrvJ9zcHAwysrKYmBgIEpLS3PZLgAAcAmZiDbI6UrRyZMno6OjI+rr60eM19fXx759+8657oknnohXX301HnzwwfN6nqGhoRgcHBxxAwAAmAg5RVFfX1+cPn06ysvLR4yXl5dHb2/vmGt+//vfx7p162L79u1RWFh4Xs/T0tISZWVlw7e5c+fmsk0AAIDzltcvWigoKBhxP8uyUWMREadPn4477rgjNm7cGNdff/15P/769etjYGBg+Hb06NF8tgkAAPCBzu/Szf8za9asmD59+qirQsePHx919Sgi4sSJE3HgwIHo7OyMb33rWxERcebMmciyLAoLC2Pnzp1x8803j1pXXFwcxcXFuWwNAAAgLzldKSoqKorq6upob28fMd7e3h61tbWj5peWlsZvfvOb6OrqGr41NTXFpz71qejq6orFixdf2O4BAAAuUE5XiiIimpub484774yamppYsmRJ/PSnP43u7u5oamqKiPfe+vbHP/4xfvazn8W0adNi/vz5I9ZfeeWVUVJSMmocAADgYsg5ihoaGqK/vz82bdoUPT09MX/+/Ghra4vKysqIiOjp6fnA7ywCAAD4sMj5e4ouBt9TBAAARHwIvqcIAADgUiOKAACApIkiAAAgaaIIAABImigCAACSJooAAICkiSIAACBpoggAAEiaKAIAAJImigAAgKSJIgAAIGmiCAAASJooAgAAkiaKAACApIkiAAAgaaIIAABImigCAACSJooAAICkiSIAACBpoggAAEiaKAIAAJImigAAgKSJIgAAIGmiCAAASJooAgAAkiaKAACApIkiAAAgaaIIAABImigCAACSJooAAICkiSIAACBpoggAAEiaKAIAAJImigAAgKSJIgAAIGmiCAAASJooAgAAkiaKAACApIkiAAAgaaIIAABImigCAACSJooAAICkiSIAACBpoggAAEiaKAIAAJImigAAgKSJIgAAIGmiCAAASJooAgAAkiaKAACApIkiAAAgaaIIAABImigCAACSJooAAICkiSIAACBpoggAAEiaKAIAAJImigAAgKSJIgAAIGmiCAAASJooAgAAkiaKAACApIkiAAAgaaIIAABImigCAACSJooAAICkiSIAACBpoggAAEiaKAIAAJImigAAgKSJIgAAIGmiCAAASJooAgAAkiaKAACApIkiAAAgaaIIAABImigCAACSJooAAICkiSIAACBpoggAAEiaKAIAAJImigAAgKTlFUWbN2+OqqqqKCkpierq6tizZ8855z733HNx6623xsc//vEoLS2NJUuWxC9+8Yu8NwwAADCeco6i1tbWWLNmTWzYsCE6Ozujrq4uli5dGt3d3WPO3717d9x6663R1tYWHR0dcdNNN8Xy5cujs7PzgjcPAABwoQqyLMtyWbB48eJYuHBhbNmyZXhs3rx5sWLFimhpaTmvx/jMZz4TDQ0N8cADD5zX/MHBwSgrK4uBgYEoLS3NZbsAAMAlZCLaIKcrRSdPnoyOjo6or68fMV5fXx/79u07r8c4c+ZMnDhxIq644opzzhkaGorBwcERNwAAgImQUxT19fXF6dOno7y8fMR4eXl59Pb2ntdj/OhHP4q33347Vq5cec45LS0tUVZWNnybO3duLtsEAAA4b3n9ooWCgoIR97MsGzU2lqeffjq+//3vR2tra1x55ZXnnLd+/foYGBgYvh09ejSfbQIAAHygwlwmz5o1K6ZPnz7qqtDx48dHXT36a62trbFq1arYsWNH3HLLLe87t7i4OIqLi3PZGgAAQF5yulJUVFQU1dXV0d7ePmK8vb09amtrz7nu6aefjrvvvjueeuqpuP322/PbKQAAwATI6UpRRERzc3PceeedUVNTE0uWLImf/vSn0d3dHU1NTRHx3lvf/vjHP8bPfvaziHgviBobG+M//uM/4vOf//zwVabLLrssysrKxvGlAAAA5C7nKGpoaIj+/v7YtGlT9PT0xPz586OtrS0qKysjIqKnp2fEdxb95Cc/iVOnTsU3v/nN+OY3vzk8ftddd8WT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",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA0UAAAH/CAYAAACYSXaPAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAIKlJREFUeJzt3X9s1fW9+PFXobTV7baLMGsR7OquTjYydmkDo65ZdFoDhhtuttDFxaoXkzXbLhd63Qay6CBLmrubmXudglsEzRL0Nvgr/tE5mps7fgg3GU27LEK2RZiF2UpasxZ1KwKf+4df+r1di3IObbG8H4/k/HHevN/nvI952/Dkc05PQZZlWQAAACRq2sXeAAAAwMUkigAAgKSJIgAAIGmiCAAASJooAgAAkiaKAACApIkiAAAgaaIIAABImigCAACSJooAAICk5RxFu3fvjuXLl8fs2bOjoKAgXnjhhQ9cs2vXrqiuro6SkpK49tpr47HHHstnrwAAAOMu5yh6++23Y8GCBfHII4+c1/wjR47EsmXLoq6uLjo7O+P++++P1atXx7PPPpvzZgEAAMZbQZZlWd6LCwri+eefjxUrVpxzzne/+9148cUX49ChQ8NjTU1N8etf/zr279+f71MDAACMi8KJfoL9+/dHfX39iLHbbrsttm7dGu+++27MmDFj1JqhoaEYGhoavn/mzJl48803Y+bMmVFQUDDRWwYAAD6ksiyLEydOxOzZs2PatPH5FQkTHkW9vb1RXl4+Yqy8vDxOnToVfX19UVFRMWpNS0tLbNy4caK3BgAATFFHjx6NOXPmjMtjTXgURcSoqztn37F3rqs+69evj+bm5uH7AwMDcc0118TRo0ejtLR04jYKAAB8qA0ODsbcuXPjb/7mb8btMSc8iq666qro7e0dMXb8+PEoLCyMmTNnjrmmuLg4iouLR42XlpaKIgAAYFw/VjPh31O0ZMmSaG9vHzG2c+fOqKmpGfPzRAAAAJMp5yh66623oqurK7q6uiLivV+53dXVFd3d3RHx3lvfGhsbh+c3NTXFa6+9Fs3NzXHo0KHYtm1bbN26Ne67777xeQUAAAAXIOe3zx04cCBuuumm4ftnP/tz1113xZNPPhk9PT3DgRQRUVVVFW1tbbF27dp49NFHY/bs2fHwww/Hl7/85XHYPgAAwIW5oO8pmiyDg4NRVlYWAwMDPlMEAAAJm4g2mPDPFAEAAHyYiSIAACBpoggAAEiaKAIAAJImigAAgKSJIgAAIGmiCAAASJooAgAAkiaKAACApIkiAAAgaaIIAABImigCAACSJooAAICkiSIAACBpoggAAEiaKAIAAJImigAAgKSJIgAAIGmiCAAASJooAgAAkiaKAACApIkiAAAgaaIIAABImigCAACSJooAAICkiSIAACBpoggAAEiaKAIAAJImigAAgKSJIgAAIGmiCAAASJooAgAAkiaKAACApIkiAAAgaaIIAABImigCAACSJooAAICkiSIAACBpoggAAEiaKAIAAJImigAAgKSJIgAAIGmiCAAASJooAgAAkiaKAACApIkiAAAgaaIIAABImigCAACSJooAAICkiSIAACBpoggAAEiaKAIAAJImigAAgKSJIgAAIGmiCAAASJooAgAAkiaKAACApIkiAAAgaaIIAABImigCAACSJooAAICkiSIAACBpoggAAEiaKAIAAJImigAAgKSJIgAAIGmiCAAASJooAgAAkiaKAACApIkiAAAgaaIIAABImigCAACSJooAAICkiSIAACBpoggAAEiaKAIAAJImigAAgKSJIgAAIGmiCAAASJooAgAAkiaKAACApOUVRZs3b46qqqooKSmJ6urq2LNnz/vO3759eyxYsCAuv/zyqKioiHvuuSf6+/vz2jAAAMB4yjmKWltbY82aNbFhw4bo7OyMurq6WLp0aXR3d485f+/evdHY2BirVq2KV155JXbs2BG/+tWv4t57773gzQMAAFyonKPooYceilWrVsW9994b8+bNi3//93+PuXPnxpYtW8ac/z//8z/xiU98IlavXh1VVVXxhS98Ib7+9a/HgQMHLnjzAAAAFyqnKDp58mR0dHREfX39iPH6+vrYt2/fmGtqa2vj2LFj0dbWFlmWxRtvvBHPPPNM3H777fnvGgAAYJzkFEV9fX1x+vTpKC8vHzFeXl4evb29Y66pra2N7du3R0NDQxQVFcVVV10VH/vYx+LHP/7xOZ9naGgoBgcHR9wAAAAmQl6/aKGgoGDE/SzLRo2ddfDgwVi9enU88MAD0dHRES+99FIcOXIkmpqazvn4LS0tUVZWNnybO3duPtsEAAD4QAVZlmXnO/nkyZNx+eWXx44dO+If/uEfhsf/+Z//Obq6umLXrl2j1tx5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QNJEEQAAkDRRBAAAJE0UAQAASRNFAABA0kQRAACQNFEEAAAkTRQBAABJE0UAAEDSRBEAAJA0UQQAACRNFAEAAEkTRQAAQNJEEQAAkDRRBAAAJE0UAQAASRNFAABA0kQRAACQNFEEAAAkTRQBAABJE0UAAEDSRBEAAJA0UQQAACQtryjavHlzVFVVRUlJSVRXV8eePXvOa93LL78chYWF8bnPfS6fpwUAABh3OUdRa2trrFmzJjZs2BCdnZ1RV1cXS5cuje7u7vddNzAwEI2NjfGlL30p780CAACMt4Isy7JcFixevDgWLlwYW7ZsGR6bN29erFixIlpaWs657qtf/Wpcd911MX369HjhhReiq6vrvJ9zcHAwysrKYmBgIEpLS3PZLgAAcAmZiDbI6UrRyZMno6OjI+rr60eM19fXx759+8657oknnohXX301HnzwwfN6nqGhoRgcHBxxAwAAmAg5RVFfX1+cPn06ysvLR4yXl5dHb2/vmGt+//vfx7p162L79u1RWFh4Xs/T0tISZWVlw7e5c+fmsk0AAIDzltcvWigoKBhxP8uyUWMREadPn4477rgjNm7cGNdff/15P/769etjYGBg+Hb06NF8tgkAAPCBzu/Szf8za9asmD59+qirQsePHx919Sgi4sSJE3HgwIHo7OyMb33rWxERcebMmciyLAoLC2Pnzp1x8803j1pXXFwcxcXFuWwNAAAgLzldKSoqKorq6upob28fMd7e3h61tbWj5peWlsZvfvOb6OrqGr41NTXFpz71qejq6orFixdf2O4BAAAuUE5XiiIimpub484774yamppYsmRJ/PSnP43u7u5oamqKiPfe+vbHP/4xfvazn8W0adNi/vz5I9ZfeeWVUVJSMmocAADgYsg5ihoaGqK/vz82bdoUPT09MX/+/Ghra4vKysqIiOjp6fnA7ywCAAD4sMj5e4ouBt9TBAAARHwIvqcIAADgUiOKAACApIkiAAAgaaIIAABImigCAACSJooAAICkiSIAACBpoggAAEiaKAIAAJImigAAgKSJIgAAIGmiCAAASJooAgAAkiaKAACApIkiAAAgaaIIAABImigCAACSJooAAICkiSIAACBpoggAAEiaKAIAAJImigAAgKSJIgAAIGmiCAAASJooAgAAkiaKAACApIkiAAAgaaIIAABImigCAACSJooAAICkiSIAACBpoggAAEiaKAIAAJImigAAgKSJIgAAIGmiCAAASJooAgAAkiaKAACApIkiAAAgaaIIAABImigCAACSJooAAICkiSIAACBpoggAAEiaKAIAAJImigAAgKSJIgAAIGmiCAAASJooAgAAkiaKAACApIkiAAAgaaIIAABImigCAACSJooAAICkiSIAACBpoggAAEiaKAIAAJImigAAgKSJIgAAIGmiCAAASJooAgAAkiaKAACApIkiAAAgaaIIAABImigCAACSJooAAICkiSIAACBpoggAAEiaKAIAAJImigAAgKSJIgAAIGmiCAAASJooAgAAkiaKAACApIkiAAAgaaIIAABImigCAACSJooAAICkiSIAACBpoggAAEiaKAIAAJImigAAgKTlFUWbN2+OqqqqKCkpierq6tizZ8855z733HNx6623xsc//vEoLS2NJUuWxC9+8Yu8NwwAADCeco6i1tbWWLNmTWzYsCE6Ozujrq4uli5dGt3d3WPO3717d9x6663R1tYWHR0dcdNNN8Xy5cujs7PzgjcPAABwoQqyLMtyWbB48eJYuHBhbNmyZXhs3rx5sWLFimhpaTmvx/jMZz4TDQ0N8cADD5zX/MHBwSgrK4uBgYEoLS3NZbsAAMAlZCLaIKcrRSdPnoyOjo6or68fMV5fXx/79u07r8c4c+ZMnDhxIq644opzzhkaGorBwcERNwAAgImQUxT19fXF6dOno7y8fMR4eXl59Pb2ntdj/OhHP4q33347Vq5cec45LS0tUVZWNnybO3duLtsEAAA4b3n9ooWCgoIR97MsGzU2lqeffjq+//3vR2tra1x55ZXnnLd+/foYGBgYvh09ejSfbQIAAHygwlwmz5o1K6ZPnz7qqtDx48dHXT36a62trbFq1arYsWNH3HLLLe87t7i4OIqLi3PZGgAAQF5yulJUVFQU1dXV0d7ePmK8vb09amtrz7nu6aefjrvvvjueeuqpuP322/PbKQAAwATI6UpRRERzc3PceeedUVNTE0uWLImf/vSn0d3dHU1NTRHx3lvf/vjHP8bPfvaziHgviBobG+M//uM/4vOf//zwVabLLrssysrKxvGlAAAA5C7nKGpoaIj+/v7YtGlT9PT0xPz586OtrS0qKysjIqKnp2fEdxb95Cc/iVOnTsU3v/nN+OY3vzk8ftddd8WT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",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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Fi1apPbt2ys/P19jx46V0+msMkdGRobS09O9+263W/Hx8YGKDAAAACAE+F2UJOnAgQOaN2+eDhw4oNdff10xMTFauXKl4uPj1b59+2oLN27cOE2YMEH33XefJKljx446fPiwMjMzqyxKdrtddru92jIAAAAACD9+v8whJydHHTt21ObNm7V06VKVlpZKkj7//HM9//zz1Rru+++/V506vhHr1q3L68EBAAAA1Ci/i9KECRP04osvKjs7W/Xr1/eOp6Sk6NNPP63WcKmpqZoyZYpWrFihQ4cOadmyZZo2bZpuv/32av0cAAAAAPgxv2+927lzpxYtWnTeeNOmTfXtt99WS6hz3nzzTT377LN6/PHHVVxcLKfTqUcffVTPPfdctX4OAAAAAPyY30Xpkksu0fHjx5WUlOQzvmPHDjVv3rzagklSZGSkpk+fHtA37QEAAACA37fe3X///Ro/fryKiopks9lUUVGhf/zjH/rtb3+rIUOG1ERGAAAAAAgov4vSlClT1KJFCzVv3lylpaVq166dbrzxRnXv3l3PPPNMTWQEAAAAgIDy+9a7evXq6U9/+pNeeOEF7dixQxUVFerUqZNat25dE/kAAAAAIOB+0fcoSdLll1+uli1bSpJsNlu1BQIAAAAAq/l9650kzZ07Vx06dFCDBg3UoEEDdejQQW+//XZ1ZwMAAAAAS/h9RenZZ5/Va6+9plGjRqlbt26SpE8//VRPPPGEDh06pBdffLHaQwIAAABAIPldlGbOnKk5c+Zo0KBB3rH+/fvrqquu0qhRoyhKAAAAAGo9v2+9Ky8vV5cuXc4b79y5s86ePVstoQAAAADASn4XpQceeEAzZ848b3z27NkaPHhwtYQCAAAAACv9orfezZ07V6tXr9b1118vSdq0aZMKCws1ZMgQpaene+dNmzatelICAAAAQAD5XZR27dqla665RpJ04MABSVLTpk3VtGlT7dq1yzuPV4YDAAAAqK38Lkrr1q2riRwAAAAAEDR+0fcoAQAAAEAoC/qilJiYKJvNdt42YsQIq6MBAAAACFG/6GUOgbR161aVl5d793ft2qVf//rXuvvuuy1MBQAAACCUBX1Ratq0qc/+1KlTdfnll6tnz54WJQIAAAAQ6oL+1rsfO336tBYuXKhhw4bxVj0AAAAANSboryj9WFZWlk6ePKmhQ4dWOcfj8cjj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p0+f1nfffVflHKtRlAKgfv366ty5s7Kzs33Gs7Oz1b17d4tSBZdzf7n8eI1Onz6tnJyckF8jwzA0cuRILV26VB9//LGSkpJ8jofz2lTGMAx5PJ6wXpfevXtr586dys/P925dunTR4MGDlZ+fr5YtW4bt2ph5PB7t3r1bcXFxYf1n5oYbbjjvawf27t2rhIQESfw9I0nz5s1TTEyM+vXr5x0L53X5/vvvVaeO7z8T69at6309eDivzTmNGjVSXFycvvvuO61atUoDBgxgXf7Pz1mHzp07q169ej5zjh8/rl27dgXPWlnwAomwdO714HPnzjW+/PJLY+zYsUajRo2MQ4cOWR0tYE6dOmXs2LHD2LFjhyHJmDZtmrFjxw7vK9KnTp1qOBwOY+nSpcbOnTuNQYMGheTrNM0ee+wxw+FwGOvXr/d5Re3333/vnROua5ORkWHk5uYaBQUFxueff248/fTTRp06dYzVq1cbhhG+61KZH7/1zjDCd22efPJJY/369cbBgweNTZs2GbfddpsRGRnp/bs2XNdly5YtRkREhDFlyhRj3759xp/+9CfjoosuMhYuXOidE65rYxiGUV5ebrRo0cIYP378ecfCdV3S0tKM5s2be18PvnTpUqNJkybGU0895Z0TrmuzcuVK46OPPjIOHjxorF692khOTjauvfZa4/Tp04ZhhM+6VMe/64YPH25cdtllxpo1a4zt27cbN910E68HD1f/8z//YyQkJBj169c3rrnmGu/rn8PFunXrDEnnbWlpaYZh/PtVks8//7wRGxtr2O1248YbbzR27txpbegAqGxNJBnz5s3zzgnXtRk2bJj3fzNNmzY1evfu7S1JhhG+61IZc1EK17U59z0d9erVM5xOp3HHHXcYX3zxhfd4uK6LYRjG3//+d6NDhw6G3W432rRpY8yePdvneDivzapVqwxJxp49e847Fq7r4na7jTFjxhgtWrQwGjRoYLRs2dKYOHGi4fF4vHPCdW2WLFlitGzZ0qhfv74RGxtrjBgxwjh58qT3eLisS3X8u+6HH34wRo4caURHRxsNGzY0brvtNuPIkSMW/DaVsxmGYQT4IhYAAAAABDWeUQIAAAAAE4oSAAAAAJhQlAAAAADAhKIEAAAAACYUJQAAAAAwoSgBAAAAgAlFCQAAAABMKEoAAAAAYEJRAgAAAAATihIAAD9y5swZqyMAAIIARQkAUCv87W9/U8eOHdWwYUM1btxYffr0UVlZmSTpnXfeUfv27WW32xUXF6eRI0d6zzty5IgGDBigiy++WFFRUbrnnnv09ddfe49PmjRJV199td555x21bNlSdrtdhmGopKREjzzyiGJiYhQVFaWbbrpJn332WcB/bwCANShKAICgd/z4cQ0aNEjDhg3T7t27tX79et1xxx0yDEMzZ87UiBEj9Mgjj2jnzp1avny5WrVqJUkyDEMDBw7UiRMnlJOTo+zsbB04cED33nuvz8/fv3+//vKXv+i9995Tfn6+JKlfv34qKirShx9+qG3btumaa65R7969deLEiUD/+gAAC9gMwzCsDgEAwIVs375dnTt31qFDh5SQkOBzrHnz5nrooYf04osvnndedna2XC6XCgoKFB8fL0n68ssv1b59e23ZskVdu3bVpEmT9NJLL+no0aNq2rSpJOnjjz/W7bffruLiYtntdu/Pa9WqlZ566ik98sgjNfjbAgCCQYTVAQAA+CnJycnq3bu3OnbsqJtvvll9+/bVXXfdpTNnzujYsWPq3bt3peft3r1b8fHx3pIkSe3atdMll1yi3bt3q2vXrpKkhIQEb0mSpG3btqm0tFSNGzf2+Xk//PCDDhw4UAO/IQAg2FCUAABBr27dusrOztbGjRu1evVqvfnmm5o4caLWrl17wfMMw5DNZvvJ8UaNGvkcr6ioUFxcnNavX3/euZdccskv+h0AALULRQkAUCvYbDbdcMMNuuGGG/Tcc88pISFB2dnZSkxM1Nq1a5WSknLeOe3atdORI0dUWFjoc+tdSUmJ2rZtW+VnXXPNNSoqKlJERIQSExNr6lcCAAQxihIAIOht3rxZa9euVd++fRUTE6PNmzfrn//8p9q2batJkyZp+PDhiomJkcvl0qlTp/SPf/xDo0aNUp8+fXTVVVdp8ODBmj59us6ePavHH39cPXv2VJcuXar8vD59+qhbt24aOHCgXn75ZV155ZU6duyYPvzwQw0cOPCC5wIAQgNFCQAQ9KKiopSbm6vp06fL7XYrISFBr776qlwulyTpX//6l1577TX99re/VZMmTXTXXXdJ+vdVqKysLI0aNUo33nij6tSpo1tuuUVvvvnmBT/PZrPpww8/1MSJEzVs2DD985//VGxsrG688UY1a9asxn9fAID1eOsdAAAAAJjwPUoAAAAAYEJRAgAAAAATihIAAAAAmFCUAAAAAMCEogQAAAAAJhQlAAAAADChKAEAAACACUUJAAAAAEwoSgAAAABgQlECAAAAABOKEgAAAACYUJQAAAAAwOT/AZ68G1G4FQ0GAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig=plt.figure(figsize=(10,6))\n",
    "ax=fig.add_subplot(111)\n",
    "freq,_,_=ax.hist(english_scores,bins=10,range=(0,100))\n",
    "ax.set_xlabel('score')\n",
    "ax.set_ylabel('person number')\n",
    "ax.set_xticks(np.linspace(0,100,10+1))\n",
    "ax.set_yticks(np.arange(0,freq.max()+1))\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "id": "24c318d1-2990-430c-8ae2-c22cdb452904",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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Z8+eqKmpieLi4rjxxhvjqaeeGqaVMtrl2Wsvv/xy3HHHHfHZz342SkpKYsGCBfHTn/50GFfLaJb399pFb7zxRhQWFsaXvvSlq7tAxoy8e623tzfWr18fM2bMiKKiovj85z8fO3bsGKbVMprl3Ws7d+6M2bNnx7XXXhvl5eXxwAMPxKlTp4ZptYxGe/fujSVLlsS0adOioKAgXn311U8859PaBZ+K0Nq1a1esXr061q9fH62trVFbWxuLFy/u9zGLv+vYsWNx1113RW1tbbS2tsYjjzwSq1atipdeemmYV85ok3ev7d27N+64445oamqKlpaWuPXWW2PJkiXR2to6zCtntMm71y46ffp0rFixIr761a8O00oZ7Yay15YtWxb/+q//Gtu3b4//+q//iueffz5uueWWYVw1o1HevbZ///5YsWJFrFy5Mt5888144YUX4mc/+1k8+OCDw7xyRpP3338/Zs+eHU8++eQVzf9Ud0H2KTBv3rysvr6+39gtt9ySrV27dtD5f/u3f5vdcsst/ca++c1vZl/+8pev2hoZG/LutcFUV1dnmzZtSr00xpih7rXly5dnf/d3f5dt2LAhmz179lVcIWNF3r32L//yL1lpaWl26tSp4VgeY0jevfYP//AP2Y033thv7IknnsgqKiqu2hoZWyIie+WVVy4759PcBSN+R+vs2bPR0tISdXV1/cbr6uriwIEDg55z8ODBAfPvvPPOOHToUHz44YdXba2MbkPZax934cKF6OnpicmTJ1+NJTJGDHWvPfPMM/HWW2/Fhg0brvYSGSOGstdee+21mDt3bnzve9+L6dOnx8033xwPPfRQ/Pa3vx2OJTNKDWWvLVy4MDo6OqKpqSmyLIt33nknXnzxxbj77ruHY8n8gfg0d0HhiF49Irq7u+P8+fNRVlbWb7ysrCy6uroGPaerq2vQ+efOnYvu7u4oLy+/autl9BrKXvu473//+/H+++/HsmXLrsYSGSOGstd+/etfx9q1a2Pfvn1RWDjiv5oZJYay144ePRr79++P4uLieOWVV6K7uzu+9a1vxbvvvut9WlzSUPbawoULY+fOnbF8+fL43//93zh37lz8xV/8RfzgBz8YjiXzB+LT3AUjfkfrooKCgn7HWZYNGPuk+YONw8fl3WsXPf/887Fx48bYtWtXXH/99VdreYwhV7rXzp8/H/fcc09s2rQpbr755uFaHmNInt9rFy5ciIKCgti5c2fMmzcv7rrrrnj88cfj2WefdVeLT5Rnr7W1tcWqVavi0UcfjZaWlnj99dfj2LFjUV9fPxxL5Q/Ip7ULRvx/m06dOjXGjx8/4P+GnDx5ckCdXnTDDTcMOr+wsDCmTJly1dbK6DaUvXbRrl27YuXKlfHCCy/E7bfffjWXyRiQd6/19PTEoUOHorW1Nb7zne9ExEf/GM6yLAoLC2P37t1x2223DcvaGV2G8nutvLw8pk+fHqWlpX1jM2fOjCzLoqOjI2666aarumZGp6HstcbGxli0aFE8/PDDERHxxS9+Ma677rqora2Nxx57zBNIJPFp7oIRv6M1ceLEqKmpiebm5n7jzc3NsXDhwkHPWbBgwYD5u3fvjrlz58aECROu2loZ3Yay1yI+upN1//33x3PPPee5cq5I3r1WUlISv/jFL+Lw4cN9r/r6+vjCF74Qhw8fjvnz5w/X0hllhvJ7bdGiRfGb3/wm3nvvvb6xX/3qVzFu3LioqKi4qutl9BrKXvvggw9i3Lj+/9QcP358RPzfHQf4fX2qu2CEPoSjn5/85CfZhAkTsu3bt2dtbW3Z6tWrs+uuuy777//+7yzLsmzt2rXZvffe2zf/6NGj2bXXXputWbMma2try7Zv355NmDAhe/HFF0fqj8AokXevPffcc1lhYWG2ZcuWrLOzs+/1P//zPyP1R2CUyLvXPs6nDnKl8u61np6erKKiIvv617+evfnmm9mePXuym266KXvwwQdH6o/AKJF3rz3zzDNZYWFhtnXr1uytt97K9u/fn82dOzebN2/eSP0RGAV6enqy1tbWrLW1NYuI7PHHH89aW1uzt99+O8uy0dUFn4rQyrIs27JlSzZjxoxs4sSJ2Zw5c7I9e/b0/bf77rsv+8pXvtJv/r//+79nf/Znf5ZNnDgx+9znPpdt27ZtmFfMaJVnr33lK1/JImLA67777hv+hTPq5P299ruEFnnk3WtHjhzJbr/99uyaa67JKioqsoaGhuyDDz4Y5lUzGuXda0888URWXV2dXXPNNVl5eXn2l3/5l1lHR8cwr5rR5N/+7d8u+2+v0dQFBVnm3i0AAEBKI/4eLQAAgLFGaAEAACQmtAAAABITWgAAAIkJLQAAgMSEFgAAQGJCCwAAIDGhBQAAkJjQAgAASExoAQAAJCa0AAAAEhNaAAAAif0/AT9rm/z5AFsAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 1000x600 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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Z8+eqKmpieLi4rjxxhvjqaeeGqaVMtrl2Wsvv/xy3HHHHfHZz342SkpKYsGCBfHTn/50GFfLaJb399pFb7zxRhQWFsaXvvSlq7tAxoy8e623tzfWr18fM2bMiKKiovj85z8fO3bsGKbVMprl3Ws7d+6M2bNnx7XXXhvl5eXxwAMPxKlTp4ZptYxGe/fujSVLlsS0adOioKAgXn311U8859PaBZ+K0Nq1a1esXr061q9fH62trVFbWxuLFy/u9zGLv+vYsWNx1113RW1tbbS2tsYjjzwSq1atipdeemmYV85ok3ev7d27N+64445oamqKlpaWuPXWW2PJkiXR2to6zCtntMm71y46ffp0rFixIr761a8O00oZ7Yay15YtWxb/+q//Gtu3b4//+q//iueffz5uueWWYVw1o1HevbZ///5YsWJFrFy5Mt5888144YUX4mc/+1k8+OCDw7xyRpP3338/Zs+eHU8++eQVzf9Ud0H2KTBv3rysvr6+39gtt9ySrV27dtD5f/u3f5vdcsst/ca++c1vZl/+8pev2hoZG/LutcFUV1dnmzZtSr00xpih7rXly5dnf/d3f5dt2LAhmz179lVcIWNF3r32L//yL1lpaWl26tSp4VgeY0jevfYP//AP2Y033thv7IknnsgqKiqu2hoZWyIie+WVVy4759PcBSN+R+vs2bPR0tISdXV1/cbr6uriwIEDg55z8ODBAfPvvPPOOHToUHz44YdXba2MbkPZax934cKF6OnpicmTJ1+NJTJGDHWvPfPMM/HWW2/Fhg0brvYSGSOGstdee+21mDt3bnzve9+L6dOnx8033xwPPfRQ/Pa3vx2OJTNKDWWvLVy4MDo6OqKpqSmyLIt33nknXnzxxbj77ruHY8n8gfg0d0HhiF49Irq7u+P8+fNRVlbWb7ysrCy6uroGPaerq2vQ+efOnYvu7u4oLy+/autl9BrKXvu473//+/H+++/HsmXLrsYSGSOGstd+/etfx9q1a2Pfvn1RWDjiv5oZJYay144ePRr79++P4uLieOWVV6K7uzu+9a1vxbvvvut9WlzSUPbawoULY+fOnbF8+fL43//93zh37lz8xV/8RfzgBz8YjiXzB+LT3AUjfkfrooKCgn7HWZYNGPuk+YONw8fl3WsXPf/887Fx48bYtWtXXH/99VdreYwhV7rXzp8/H/fcc09s2rQpbr755uFaHmNInt9rFy5ciIKCgti5c2fMmzcv7rrrrnj88cfj2WefdVeLT5Rnr7W1tcWqVavi0UcfjZaWlnj99dfj2LFjUV9fPxxL5Q/Ip7ULRvx/m06dOjXGjx8/4P+GnDx5ckCdXnTDDTcMOr+wsDCmTJly1dbK6DaUvXbRrl27YuXKlfHCCy/E7bfffjWXyRiQd6/19PTEoUOHorW1Nb7zne9ExEf/GM6yLAoLC2P37t1x2223DcvaGV2G8nutvLw8pk+fHqWlpX1jM2fOjCzLoqOjI2666aarumZGp6HstcbGxli0aFE8/PDDERHxxS9+Ma677rqora2Nxx57zBNIJPFp7oIRv6M1ceLEqKmpiebm5n7jzc3NsXDhwkHPWbBgwYD5u3fvjrlz58aECROu2loZ3Yay1yI+upN1//33x3PPPee5cq5I3r1WUlISv/jFL+Lw4cN9r/r6+vjCF74Qhw8fjvnz5w/X0hllhvJ7bdGiRfGb3/wm3nvvvb6xX/3qVzFu3LioqKi4qutl9BrKXvvggw9i3Lj+/9QcP358RPzfHQf4fX2qu2CEPoSjn5/85CfZhAkTsu3bt2dtbW3Z6tWrs+uuuy777//+7yzLsmzt2rXZvffe2zf/6NGj2bXXXputWbMma2try7Zv355NmDAhe/HFF0fqj8AokXevPffcc1lhYWG2ZcuWrLOzs+/1P//zPyP1R2CUyLvXPs6nDnKl8u61np6erKKiIvv617+evfnmm9mePXuym266KXvwwQdH6o/AKJF3rz3zzDNZYWFhtnXr1uytt97K9u/fn82dOzebN2/eSP0RGAV6enqy1tbWrLW1NYuI7PHHH89aW1uzt99+O8uy0dUFn4rQyrIs27JlSzZjxoxs4sSJ2Zw5c7I9e/b0/bf77rsv+8pXvtJv/r//+79nf/Znf5ZNnDgx+9znPpdt27ZtmFfMaJVnr33lK1/JImLA67777hv+hTPq5P299ruEFnnk3WtHjhzJbr/99uyaa67JKioqsoaGhuyDDz4Y5lUzGuXda0888URWXV2dXXPNNVl5eXn2l3/5l1lHR8cwr5rR5N/+7d8u+2+v0dQFBVnm3i0AAEBKI/4eLQAAgLFGaAEAACQmtAAAABITWgAAAIkJLQAAgMSEFgAAQGJCCwAAIDGhBQAAkJjQAgAASExoAQAAJCa0AAAAEhNaAAAAif0/AT9rm/z5AFsAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 1000x600 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 1000x600 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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b968UuWRkZH685//TDIJAADK7bPPPlNsbKwuvPBC2Ww2tv8AgEpUr149/fnPf66w9rz+c9/u3bvLfHEzLi5ODoejQoICAAC13+7du7V+/Xq9/fbbOnjwoNXhAECt95///Ef9+/dXs2bNtHv3bknSP//5T3344Yc+ted1MhkZGanNmzeXKv/hhx/UuHFjn4IAAAB1i2maWrFihSSpR48eatSokcURAUDtNnfuXCUnJ2vYsGE6ePCgnE6nJKlhw4aaPXu2T216nUxef/31uvvuu7Vy5Uo5nU45nU59+eWXuueee3T99df7FAQAAKhbtmzZol9//VUBAQG69NJLrQ4HAGq9f/3rX3rppZc0depU+fn9723HxMREbdmyxac2vU4mH330UfXq1UuXXXaZgoODFRwcrKSkJA0aNEiPP/641wHMmTNH8fHxCgoKUkJCglavXn3GullZWbrxxhvVrl072Ww2TZw4sVSdl156SQMGDFDDhg3VsGFDDR48WBs2bPCoM23aNBmG4XFER0d7HTsAAPBecXGxvvjiC0lS//79Vb9+fYsjAoDaLyMjQ927dy9VHhgYqIKCAp/a9DqZDAgI0JIlS/Tzzz/rjTfe0HvvvaedO3dq4cKFCggI8KqtJUuWaOLEiZo6darS0tI0YMAADRs27IzvXhYWFioiIkJTp051L2d7uq+++ko33HCDVq5cqXXr1ik2NlZJSUnat2+fR72OHTsqKyvLffiajQMAAO+sX79eeXl5CgsLU+/eva0OBwDqhPj4eG3atKlU+aeffqoOHTr41KbP621fcMEFuu6663TllVcqLi7OpzZmzZqlcePGafz48Wrfvr1mz56tmJgYzZ07t8z6LVu21HPPPaexY8cqPDy8zDpvvPGG7rjjDnXr1k0XXnihXnrpJblcLvdfQE/y8/NTdHS0+4iIiPDpHgAAQPkdO3ZMa9askSRddtll8vf3tzgiALCON7M0pRODa1OnTlVcXJwCAwPVunVrLVy4sFx93Xfffbrzzju1ZMkSmaapDRs26LHHHtPf//533XfffT7F7/XWIE6nU6+++qq++OIL5eTkyOVyeXz+5ZdflqudoqIipaamasqUKR7lSUlJWrt2rbdhndHRo0dVXFxc6sX+HTt2qFmzZgoMDFSvXr30+OOPq1WrVhXWLwAAKC04OFjXXXedtmzZos6dO1sdDgBY5uQszTlz5qhfv3568cUXNWzYMG3dulWxsbFlXjNq1Cjt379fCxYsUJs2bZSTk6OSkpJy9XfrrbeqpKRE999/v44ePaobb7xRzZs313PPPefz2jdeJ5P33HOPXn31VV1xxRXq1KmTDMPwqePc3Fw5nU5FRUV5lEdFRSk7O9unNssyZcoUNW/eXIMHD3aX9erVS4sWLdIFF1yg/fv369FHH1Xfvn31008/nXFF2sLCQhUWFrrP8/PzKyxGAADqkjZt2qhNmzZWhwEAljp1lqYkzZ49W5999pnmzp2rmTNnlqq/fPlyrVq1Srt27XIPlJV3b96SkhK98cYbGjFihG6//Xbl5ubK5XIpMjLyvO7B62Tyrbfe0tKlSzV8+PDz6vik05NR0zR9TlBP99RTT2nx4sX66quvFBQU5C4fNmyY++vOnTurT58+at26tV577TUlJyeX2dbMmTM1ffr0CokLAIC66Pjx4x4/jwGgrvJlluZHH32kxMREPfXUU/rPf/6jkJAQ/eEPf9Ajjzyi4ODgs/bn5+env/71r0pPT5ckNWnSpELuw6cFeCrir4lNmjSR3W4vNQqZk5NTarTSF88884wef/xxrVixQl26dDlr3ZCQEHXu3Fk7duw4Y50HHnhAhw8fdh9bt2497xgBAKgrdu7cqdmzZ2vdunVWhwIAlSY/P195eXnu49SZjafyZZbmrl27tGbNGv344496//33NXv2bL3zzju68847yxVbr169lJaW5t0NnYPXyeS9996r5557TqZpnlfHAQEBSkhIUEpKikd5SkqK+vbte15tP/3003rkkUe0fPlyJSYmnrN+YWGh0tPT1bRp0zPWCQwMVFhYmPsIDQ09rxgBAKgrXC6XVqxYocLCQh0+fNjqcACg0nTo0EHh4eHuo6zpqqfyZpamy+WSYRh644031LNnTw0fPlyzZs3Sq6++qmPHjp0ztjvuuEP33nuvXnjhBa1bt06bN2/2OHzh9TTXNWvWaOXKlfr000/VsWPHUquwvffee+VuKzk5WWPGjFFiYqL69Omj+fPny+FwaMKECZJOjAbu27dPixYtcl9zcjnbI0eO6LffftOmTZsUEBDgXs72qaee0oMPPqg333xTLVu2dGf29evXd+9jNXnyZI0YMUKxsbHKycnRo48+qry8PN18883efjsAAMA5bNq0STk5OQoKCtIll1xidTgAUGm2bt2q5s2bu88DAwPLrOfLLM2mTZuqefPmHrtatG/fXqZpau/evWrbtu1ZYxs9erQk6e6773aXGYbhTmCdTufZb64MXieTDRo00NVXX+11R2UZPXq0Dhw4oBkzZigrK0udOnXSsmXL3FuNZGVlldpz8tSNNlNTU/Xmm28qLi5OmZmZkk4sr1tUVKQ//vGPHtc9/PDDmjZtmiRp7969uuGGG5Sbm6uIiAj17t1b69ev93mLEwAAULaioiKtXLlSknTxxRef870eAKjJQkNDFRYWds56p87SPDW3SklJ0ciRI8u8pl+/fnr77bd15MgR9yDZ9u3bZbPZ1KJFi3P2mZGRUc67KD+vk8lXXnmlQgO44447dMcdd5T52auvvlqq7FzTa08mlWfz1ltvlSc0AABwnr755hsdOXJEDRs21EUXXWR1OABQbXg7S/PGG2/UI488oltvvVXTp09Xbm6u7rvvPt12221n/ENdjx499MUXX6hhw4Z67bXXNHnyZNWrV6/C7sHrdyalE0vLfv7553rxxRfdW2T8+uuvOnLkSIUFBgAAara8vDz3qoSDBw+Wn5/Xf8MGgFpr9OjRmj17tmbMmKFu3brp66+/Pusszfr16yslJUWHDh1SYmKi/vSnP2nEiBF6/vnnz9hHenq6CgoKJEnTp0+v8HzN63/Vd+/eraFDh8rhcKiwsFCXX365QkND9dRTT+n48eOaN29ehQYIAABqpszMTDmdTsXExKh9+/ZWhwMA1Y63szQvvPDCUguYnk23bt106623qn///jJNU88884x7iuzpHnrooXK3e5LXyeQ999yjxMRE/fDDD2rcuLG7/Oqrr3ZvuAkAANClSxc1a9bMvQIhAKBqvfrqq3r44Yf13//+V4Zh6NNPPy1zlohhGFWTTK5Zs0bffPONAgICPMrj4uK0b98+rwMAAAC1V0VtjA0A8F67du3c68XYbDZ98cUXioyMrLD2vU4mXS5XmcvG7t27l70XAQCAIm1HVGz6tCwDAKCSuFyuCm/T62Ty8ssv1+zZszV//nxJJ4ZEjxw5oocffljDhw+v8AABAEDNYcilfv6ZCjOO65K/v67droZWhwQAqCReJ5P//Oc/NXDgQHXo0EHHjx/XjTfeqB07dqhJkyZavHhxZcQIAABqiHb2XDWwHdcx00+/us691xoAoObyOpls1qyZNm3apMWLF2vjxo1yuVwaN26c/vSnP7ERMQAAdViAStTd/1dJUlpxMxXLbnFEAIDK5NOGT8HBwbrtttt02223VXQ8AACghuril6Ugo0SHXEHa7oywOhwAQCXzOplctGjRWT8fO3asz8EAAICaqb5RqA5+OZKk74pbyBRbgQBAdXPo0CG988472rlzp+677z41atRIGzduVFRUlJo3b+51ez7tM3mq4uJiHT16VAEBAapXrx7JJAAAdVCC317ZDVO/OkO11xVudTgAgNNs3rxZgwcPVnh4uDIzM3X77berUaNGev/997V79+5zDhqWxet1uw8ePOhxHDlyRNu2bVP//v1ZgAcAgDrJVI6rvo6bftpQHCMxKgkA1U5ycrJuueUW7dixQ0FBQe7yYcOG6euvv/apTZ/emTxd27Zt9cQTT+imm27Szz//XBFNAgCAGsNQujNK250Rcnr/d2oAQBX47rvv9OKLL5Yqb968ubKzs31qs8L+xbfb7fr1118rqjkAAFDDkEgCQPUVFBSkvLy8UuXbtm1TRIRvi6Z5PTL50UcfeZybpqmsrCy98MIL6tevn09BAACAmscmly4L+EXbSiLkcDUQ01sBoPoaOXKkZsyYoaVLl0qSDMOQw+HQlClTdO211/rUptfJ5FVXXeVxbhiGIiIiNGjQID377LM+BQEAAGqeDn45amHPUyPbMe07HiYn+0oCQLX1zDPPaPjw4YqMjNSxY8d0ySWXKDs7W3369NFjjz3mU5teJ5Mul8unjgAAQO0RqGJ18cuSJKUWNyeRBIBqLiwsTGvWrNGXX36pjRs3yuVyqUePHho8eLDPbVbIAjwAAKBu6eafpUDDqQOuYO10NrY6HADAOWRmZqply5YaNGiQBg0aVCFtep1MJicnl7vurFmzvG0eAABUc2HGcV1o/02S9F1xjEzelQSAaq9Vq1bq27evxowZo+uuu06NGjU67za9TibT0tK0ceNGlZSUqF27dpKk7du3y263q0ePHu56hsEPFgAAaqNE/72yGab2OMOV5QqzOhwAQDl8//33Wrx4sR599FHdc889GjJkiG666Sb94Q9/UGBgoE9ter2G94gRI3TJJZdo79692rhxozZu3Kg9e/Zo4MCBuvLKK7Vy5UqtXLlSX375pU8BAQCA6quxUaA4+yG5TOm74hZWhwMAKKcePXro6aeflsPh0KeffqrIyEj95S9/UWRkpG677Taf2jRM0zS9uaB58+ZasWKFOnbs6FH+448/Kikpqc7sNbl3717FxMRoz549atGCH6YAAO+1nPKJ1SH4wFRzW54a2Y5qS0lTq4OxVOYTV1gdAoBqoqbmBhs3btS4ceO0efNmOZ1Or6/3emQyLy9P+/fvL1Wek5Oj/Px8rwMAAAA1iaF9rvA6n0gCQE21Z88ePfXUU+rWrZsuuugihYSE6IUXXvCpLa/fmbz66qt166236tlnn1Xv3r0lSevXr9d9992na665xqcgAABA9WaXU35yqVD+VocCAPDB/Pnz9cYbb+ibb75Ru3bt9Kc//UkffPCBWrZs6XObXieT8+bN0+TJk3XTTTepuLj4RCN+fho3bpyefvppnwMBAADViyFTUbZ8BRvFambLU5z9oL4rjtUOZxOrQwMAeOmRRx7R9ddfr+eee07dunWrkDa9Tibr1aunOXPm6Omnn9bOnTtlmqbatGmjkJCQCgkIAABYL852UL38HQqxFXuUNzCOWRQRAOB8OByOCt9xw+tk8qSsrCxlZWXp4osvVnBwsEzTZDsQAABqgTjbQQ0M2Fmq3DSljn77leOqr92uhhZEBgDwxubNm9WpUyfZbDZt2bLlrHW7dOnidfteJ5MHDhzQqFGjtHLlShmGoR07dqhVq1YaP368GjRooGeffdbrIAAAQPVgyFQvf8eJr0/7G7FhnEgoe/o75ChsIFP8ERkAqrNu3bopOztbkZGR6tatmwzD0KmbeZw8NwzDp9VcvU4mJ02aJH9/fzkcDrVv395dPnr0aE2aNIlkEgCAGizKll9qauupDEOqbxQrypavbFdYFUYGAPBWRkaGIiIi3F9XNK+TyRUrVuizzz4rtX9K27ZttXv37goLDAAAVL1g48yJpC/1AADWiYuLc3+9e/du9e3bV35+nilgSUmJ1q5d61G3vLzeZ7KgoED16tUrVZ6bm6vAwECvAwAAANXHMbN8W3+Utx4AoHoYOHCgfv/991Llhw8f1sCBA31q0+tk8uKLL9aiRYvc54ZhyOVy6emnn/Y5CAAAUD3sd4WqwOWvU16p8WCa0hGXv/a7Qqs2MADAeTnTgqkHDhzweWcOr6e5Pv3007r00kv1/fffq6ioSPfff79++ukn/f777/rmm298CgIAAFQPpgx9WxyrgQE7ZZqei/CcTDA3FMey+A4A1BDXXHONpBODgLfccovHbFKn06nNmzerb9++PrXtdTLZoUMHbd68WXPnzpXdbldBQYGuueYa3XnnnWratKlPQQAAgOpjt6uB1hXHqqtflkJOeTeywPTXhuJYtgUBgBokPDxc0omRydDQUAUHB7s/CwgIUO/evXX77bf71LZXyWRxcbGSkpL04osvavr06T51CAAAqrcWtsPq4+/QLmdDbS+OULBRrGPmiamtjEgCQM3yyiuvSJJatmypyZMn+zyltSxeJZP+/v768ccfy5xrCwAAaocL/X6TYUjHFMD2HwBQSzz88MMV3qbX01zHjh2rBQsW6IknnqjwYAAAgLVCjeNqYTssSdpWEmFxNACAivTOO+9o6dKlcjgcKioq8vhs48aNXrfndTJZVFSkl19+WSkpKUpMTCw1TDpr1iyvgwAAANXDhfYTo5J7nWHKM4OsDgcAUEGef/55TZ06VTfffLM+/PBD3Xrrrdq5c6e+++473XnnnT616XUy+eOPP6pHjx6SpO3bt3t8xvRXAABqLrucauuXK0lKL4m0OBoAQEWaM2eO5s+frxtuuEGvvfaa7r//frVq1UoPPfRQmftPlke5ksnNmzerU6dOstlsWrlypU8dAQCA6q2V/XcFGk7luwK0zxVudTgAgArkcDjcW4AEBwcrPz9fkjRmzBj17t1bL7zwgtdt2spTqXv37srNPfGXylatWunAgQNedwQAAKq31vYTf5n+2RnJqq0AUMtER0e787i4uDitX79ekpSRkSHz5EbCXipXMtmgQQNlZGRIkjIzM+VyuXzqDAAAVF+fF7XRN0Vx2lHSxOpQAAAVbNCgQfr4448lSePGjdOkSZN0+eWXa/To0br66qt9arNc01yvvfZaXXLJJWratKkMw1BiYqLsdnuZdXft2uVTIAAAwFolsmu7kxVcAaA2mj9/vntQcMKECWrUqJHWrFmjESNGaMKECT61Wa5kcv78+brmmmv0yy+/6O6779btt9+u0NBQnzoEAADVi00uuWRITG0FgFrLZrPJZvvfxNRRo0Zp1KhR59VmuVdzHTp0qCQpNTVV99xzD8kkAAC1RCe/bLWy/66Nxc3lcDW0OhwAQAXZvHlzuet26dLF6/bL9c7kqV555ZUKTSTnzJmj+Ph4BQUFKSEhQatXrz5j3aysLN14441q166dbDabJk6cWGa9d999Vx06dFBgYKA6dOig999//7z6BQCgtjJk6kL7b2poOy4/gzURAKA26datm7p3765u3bqd9ejevbtP7XudTFakJUuWaOLEiZo6darS0tI0YMAADRs2TA6Ho8z6hYWFioiI0NSpU9W1a9cy66xbt06jR4/WmDFj9MMPP2jMmDEaNWqUvv32W5/7BQCgtoq1HVKIrVjHTD9lOhmVBIDaJCMjQ7t27VJGRsZZD1/XvTFMX9eBrQC9evVSjx49NHfuXHdZ+/btddVVV2nmzJlnvfbSSy9Vt27dNHv2bI/y0aNHKy8vT59++qm7bOjQoWrYsKEWL1583v2etHfvXsXExGjPnj1q0aJFua4BAOBULad8YnUIGhKwTc3s+fqhOFobS/h55o3MJ66wOgQA1URdzQ0sG5ksKipSamqqkpKSPMqTkpK0du1an9tdt25dqTaHDBnibtPXfgsLC5WXl+c+Tm7yCQBATRVuHFMze75cprSNVVwBoNb7z3/+o379+qlZs2bavXu3JGn27Nn68MMPfWqv3AvwVLTc3Fw5nU5FRUV5lEdFRSk7O9vndrOzs8/apq/9zpw5U9OnT/c5LgAAqpv2fjmSpD2uBiowAy2OpuaxYmSZ0VAAvpo7d64eeughTZw4UY899picTqckqUGDBpo9e7ZGjhzpdZs+jUxWZEZrGJ7LkJumWaqsMtr0tt8HHnhAhw8fdh9bt249rxgBALCSn5xqbT8gSUovibQ4GgBAZfvXv/6ll156SVOnTpXdbneXJyYmasuWLT616XUyOXfuXCUnJ2v48OE6dOhQqYy2vJo0aSK73V5qNDAnJ6fUqKE3oqOjz9qmr/0GBgYqLCzMfbA1CgCgJiuRTSuLWiu9JEJZLn6mAUBtl5GRUeaqrYGBgSooKPCpTa+TyYrKaAMCApSQkKCUlBSP8pSUFPXt29fbsNz69OlTqs0VK1a426ysfgEAqFkM/eoK1/riOEnnNyMIAFD9xcfHa9OmTaXKP/30U3Xo0MGnNr1+Z7IiM9rk5GSNGTNGiYmJ6tOnj+bPny+Hw6EJEyZIOjG1dN++fVq0aJH7mpPfgCNHjui3337Tpk2bFBAQ4P4G3HPPPbr44ov15JNPauTIkfrwww/1+eefa82aNeXuFwAAAABqk/vuu0933nmnjh8/LtM0tWHDBi1evFgzZ87Uyy+/7FObXieTJzPauLg4j3JfMtrRo0frwIEDmjFjhrKystSpUyctW7bM3XZWVlapvR9PTWRTU1P15ptvKi4uTpmZmZKkvn376q233tI//vEPPfjgg2rdurWWLFmiXr16lbtfAABqs77+mSoy/fRTSaSOKcDqcAAAVeDWW29VSUmJ7r//fh09elQ33nijmjdvrueee07XX3+9T216vc/kK6+8ogcffFDPPvusxo0bp5dfflk7d+50Z7S+BlLT1NW9ZAAAFceK1UDrqUjXBW2WzZDeP95Rh8zgKo8BvmM1V6B6qu65QUlJid544w0NGTJE0dHRys3NlcvlUmTk+S3A5vXIZGVktAAAoGq08/tNNkPKctYnkQSAOsLPz09//etflZ6eLunEoqQV0q4vF91+++26/fbbKyyjBQAAlc8ml9r5/SaJ7UAAoK7p1auX0tLSKvTVPq+TyenTp+umm25S69atKyyjBQAAla+l/aCCjRIVmP5yuBpYHQ4AoArdcccduvfee7V3714lJCQoJCTE4/MuXbp43abXyeS7776rGTNm6KKLLtJNN92k0aNHKyIiwuuOAQBA1brQniNJ2lYSIdP73cEAADXY6NGjJUl33323u8wwDJmmKcMw5HQ6vW7T62Ry8+bN+umnn/TGG29o1qxZSk5O1uDBg3XTTTfpqquuUr169bwOAgAAVK5GxlFF2QvkNA1tL+GPwABQ12RkZFR4m16v5nq6b775Rm+++abefvttHT9+XHl5eRUVW7VW3VdsAgBUf1W5mmuIUahOfvtll0tri1tWWb+oWKzmClRPdTU38GkBnlOFhIQoODhYAQEBys/Pr4iYAABABSswA/VtcazVYQAAahGfXpjIyMjQY489pg4dOigxMVEbN27UtGnTlJ2dXdHxAQAAAACqIa9HJvv06aMNGzaoc+fOuvXWW937TAIAgOrIVG9/hzKcjbTfVV+SYXVAAIBawutkcuDAgXr55ZfVsWPHyogHAABUoBa2w2rv95ta2X/XkuNd5JTd6pAAALWE18nk448/XhlxAACASnCh32+SpB3OJiSSAFDHHTp0SO+884527typ++67T40aNdLGjRsVFRXl02zTciWTycnJeuSRRxQSEqLk5OSz1p01a5bXQQAAgIoXahxXC9thSSf2lgQA1F2bN2/W4MGDFR4erszMTN1+++1q1KiR3n//fe3evVuLFi3yus1yJZNpaWkqLi52fw0AAKq/C+2/yTCkvc4w5ZlBVocDALBQcnKybrnlFj311FMKDQ11lw8bNkw33nijT22WK5lcuXJlmV8DAIDqyS6n2vrlSpLSSyItjgYAYLXvvvtOL774Yqny5s2b+7wrh9dbg9x2221l7idZUFCg2267zacgAABAxWplP6hAw6l8V4D2ucKtDgcAYLGgoCDl5eWVKt+2bZsiInx7FcLrZPK1117TsWPHSpUfO3bMp3m2AACg4pXIpjxXoH52RspkOxAAqPNGjhypGTNmuF9fNAxDDodDU6ZM0bXXXutTm+VezTUvL0+maco0TeXn5yso6H/vXjidTi1btkyRkUyjAQCgOshwNlKGs6FsMq0OBQBQDTzzzDMaPny4IiMjdezYMV1yySXKzs5Wnz599Nhjj/nUZrmTyQYNGsgwDBmGoQsuuKDU54ZhaPr06T4FAQAAKoMhF6OSAABJYWFhWrNmjb788ktt3LhRLpdLPXr00ODBg31us9zJ5MqVK2WapgYNGqR3331XjRo1cn8WEBCguLg4NWvWzOdAAADA+QtSsZrb85TpbCin92+zAABqqczMTLVs2VKDBg3SoEGDKqTNcv+UueSSS3TppZcqIyNDI0eO1CWXXOI++vTpQyIJAEA10M7vN10ckKFBAb9YHQoA4BzmzJmj+Ph4BQUFKSEhQatXry7Xdd988438/PzUrVu3cvfVqlUr9e/fXy+++KJ+//13HyP25PWfLOPi4mSz2XT06FH9/PPP2rx5s8cBAACsYchUO7/fJEk7nY0tjgYAcDZLlizRxIkTNXXqVKWlpWnAgAEaNmyYHA7HWa87fPiwxo4dq8suu8yr/r7//nv16dNHjz76qJo1a6aRI0fq7bffVmFhoc/34HUy+dtvv+nKK69UaGioOnbsqO7du3scAADAGrG2QwoxinXM9FOms6HV4QAAzmLWrFkaN26cxo8fr/bt22v27NmKiYnR3Llzz3rdX/7yF914443q06ePV/316NFDTz/9tBwOhz799FNFRkbqL3/5iyIjI33e4tHrZHLixIk6ePCg1q9fr+DgYC1fvlyvvfaa2rZtq48++sinIAAAwPlr75cjSdpe0kQu3pcEgGqrqKhIqampSkpK8ihPSkrS2rVrz3jdK6+8op07d+rhhx/2uW/DMDRw4EC99NJL+vzzz9WqVSu99tprPrVV7gV4Tvryyy/14Ycf6qKLLpLNZlNcXJwuv/xyhYWFaebMmbriiit8CgQAAPgu3DimpvZ8uUxpm9O3zacBAOcnPz9feXl57vPAwEAFBgaWqpebmyun06moqCiP8qioKGVnZ5fZ9o4dOzRlyhStXr1afn5ep3Fue/bs0eLFi/Xmm29qy5Yt6tOnj1544QWf2vL6z5YFBQXu/SQbNWqk33478W5G586dtXHjRp+CAAAA5+fkqOQeVwMVmKV/cQEAVL4OHTooPDzcfcycOfOs9Q3Dc/sm0zRLlUmS0+nUjTfeqOnTp5e5TWN5zJ8/X5dcconi4+P12muvadSoUdq5c6fWrFmjv/71rz616XVK265dO23btk0tW7ZUt27d9OKLL6ply5aaN2+emjZt6lMQAADgfJiqZxRLktJLIi2OBQDqrq1bt6p58+bu87JGJSWpSZMmstvtpUYhc3JySo1WSidGPL///nulpaXprrvukiS5XC6Zpik/Pz+tWLHinNt9PPLII7r++uv13HPPebUK7Nl4nUxOnDhRWVlZkqSHH35YQ4YM0RtvvKGAgAC9+uqrFRIUAADwhqEvi9oozDiuPEYlAcAyoaGhCgsLO2e9gIAAJSQkKCUlRVdffbW7PCUlRSNHjixVPywsTFu2bPEomzNnjr788ku98847io+PP2efDoejzFHP8+F1MvmnP/3J/XX37t2VmZmpn3/+WbGxsWrSpEmFBgcAAMovzwyyOgQAQDklJydrzJgxSkxMVJ8+fTR//nw5HA5NmDBBkvTAAw9o3759WrRokWw2mzp16uRxfWRkpIKCgkqVn2rz5s3q1KmTbDZbqWT0dF26dPH6Hnx/c/P/1KtXTz169DjfZgAAgA9CjeMqMe06Jn+rQwEAeGH06NE6cOCAZsyYoaysLHXq1EnLli1TXFycJCkrK+uce06eS7du3ZSdna3IyEh169ZNhmHINE335yfPDcOQ0+n0un3DPLW1M0hOTi53g7NmzfI6iJpo7969iomJ0Z49e9SiRQurwwEA1EAtp3xy3m0MDPhFMbbDWlscp1+czBCq7TKfYNV8oDqqrrnB7t27FRsbK8MwtHv37rPWPZnEeqNcI5NpaWnlaqyi5+ACAIAzCzGKFGs7JJsh5bpCrA4HAFDNnJog7t69W3379i21rUhJSYnWrl1becnkypUrvW4YAABUrnb232QzpCxnqA6ZwVaHAwCoxgYOHKisrCz3No8nHT58WAMHDvRpmqvX+0ye9Msvv+izzz7TsWPHJEnlmC0LAAAqiE0uXeB3Yq/n9JIIi6MBAFR3Z9rD8sCBAwoJ8W12i9cL8Bw4cECjRo3SypUrZRiGduzYoVatWmn8+PFq0KCBnn32WZ8CAQAA5dfSflDBRokKTH85XA2sDgcAUE1dc801kk68knjLLbd47H3pdDq1efNm9e3b16e2vR6ZnDRpkvz9/eVwOFSvXj13+ejRo7V8+XKfggAAAN5pb8+RJG0riZDp+0QjAEAtFx4ervDwcJmmqdDQUPd5eHi4oqOj9ec//1mvv/66T217PTK5YsUKffbZZ6VWKWrbtu05VwgCAADnr56K1Mh2VE7T0HamuAIAzuKVV16RJLVs2VKTJ0/2eUprWbxOJgsKCjxGJE/Kzc31GDIFAAAVy5CpKFu+go1ifVXUSpLYXxIAUC4PP/xwhbfpdTJ58cUXa9GiRXrkkUcknZh763K59PTTT2vgwIEVHiAAAJDibAfVy9+hEFuxu6zA5S9bsbTb1dDCyAAANcU777yjpUuXyuFwqKioyOOzjRs3et2e1y9ZPP3003rxxRc1bNgwFRUV6f7771enTp309ddf68knn/Q6AAAAcHZxtoMaGLBT9Yxij/J6RrEGBuxUnO2gRZEBAGqK559/XrfeeqsiIyOVlpamnj17qnHjxtq1a5eGDRvmU5teJ5MdOnTQ5s2b1bNnT11++eUqKCjQNddco7S0NLVu3dqnIAAAQNkMmerl7zjx9Wkrup887+nvkCG26AIAnNmcOXM0f/58vfDCCwoICND999+vlJQU3X333Tp8+LBPbXo1zbW4uFhJSUl68cUXNX36dJ86BAAA5Rdly/eY2no6w5DqG8WKsuUr2xVWhZEBAGoSh8Ph3gIkODhY+fn5kqQxY8aod+/eeuGFF7xu06uRSX9/f/34449lbnYJAAAqXrBx5kTSl3oAgLopOjpaBw4ckCTFxcVp/fr1kqSMjAyZpm+zW7ye5jp27FgtWLDAp84AAIB3jpnlW621vPUAAHXToEGD9PHHH0uSxo0bp0mTJunyyy/X6NGjdfXVV/vUptfJZFFRkebOnauEhAT95S9/UXJyssfhrTlz5ig+Pl5BQUFKSEjQ6tWrz1p/1apVSkhIUFBQkFq1aqV58+Z5fH7ppZfKMIxSxxVXXOGuM23atFKfR0dHex07AACVbb8rVAUuf53pj8amKR1x+Wu/K7RqAwMA1Cjz58/X1KlTJUkTJkzQq6++qvbt22v69OmaO3euT216vTXIjz/+qB49ekiStm/f7vGZt9NflyxZookTJ2rOnDnq16+fe5XYrVu3KjY2tlT9jIwMDR8+XLfffrtef/11ffPNN7rjjjsUERGha6+9VpL03nvveSxze+DAAXXt2lXXXXedR1sdO3bU559/7j632+1exQ4AQFUwZehnZ4QS/H+VaXouwnMywdxQHCtTvIICADgzm80mm+1/Y4mjRo3SqFGjzqtNr5PJlStXnleHp5o1a5bGjRun8ePHS5Jmz56tzz77THPnztXMmTNL1Z83b55iY2M1e/ZsSVL79u31/fff65lnnnEnk40aNfK45q233lK9evVKJZN+fn6MRgIAaoT6xok/kpbIJn+53OUFpr82FMeyzyQAoEybN28ud90uXbp43b7XyWRFKSoqUmpqqqZMmeJRnpSUpLVr15Z5zbp165SUlORRNmTIEC1YsEDFxcXy9y/9vsiCBQt0/fXXKyQkxKN8x44datasmQIDA9WrVy89/vjjatWq1XneFQAAFW9dcZyyXGH6zVVP9Y0iBRvFOmaemNrKiCQA4Ey6desmwzDOucCOYRhyOp1et29ZMpmbmyun06moqCiP8qioKGVnZ5d5TXZ2dpn1S0pKlJubq6ZNm3p8tmHDBv3444+lFgzq1auXFi1apAsuuED79+/Xo48+qr59++qnn35S48aNy+y7sLBQhYWF7vOTS+kCAFDZTBnKcJ6YeXPEDLI4GgBATZGRkVGp7VuWTJ50+nuWpmme9d3LsuqXVS6dGJXs1KmTevbs6VE+bNgw99edO3dWnz591Lp1a7322mtnXERo5syZ7K0JAKhSgSpRsWxyeb9eHgAAiouLq9T2LUsmmzRpIrvdXmoUMicnp9To40nR0dFl1vfz8ys1onj06FG99dZbmjFjxjljCQkJUefOnbVjx44z1nnggQc8Es19+/apQ4cO52wbAABfXeS/R83seVpXFKc9rgZWhwMAqMEWLVp01s/Hjh3rdZuWJZMBAQFKSEhQSkqKx74mKSkpGjlyZJnX9OnTx703ykkrVqxQYmJiqfclly5dqsLCQt10003njKWwsFDp6ekaMGDAGesEBgYqMDDQfZ6Xl3fOdgEA8FV9o1Ct7QdkM6RjpuUTiQAANdw999zjcV5cXKyjR48qICBA9erV8ymZtHTeTHJysl5++WUtXLhQ6enpmjRpkhwOhyZMmCDpxGjgqTc1YcIE7d69W8nJyUpPT9fChQu1YMECTZ48uVTbCxYs0FVXXVXmO5CTJ0/WqlWrlJGRoW+//VZ//OMflZeXp5tvvrnybhYAAC908suWzZD2OUOVa9a3OhwAQA138OBBj+PIkSPatm2b+vfvr8WLF/vUpqV/6hw9erQOHDigGTNmKCsrS506ddKyZcvcc3uzsrLkcDjc9ePj47Vs2TJNmjRJ//73v9WsWTM9//zz7m1BTtq+fbvWrFmjFStWlNnv3r17dcMNNyg3N1cRERHq3bu31q9fX+lzigEAKI9gFamtPVeStLmk6TlqAwDgm7Zt2+qJJ57QTTfdpJ9//tnr6w3zXOvEokx79+5VTEyM9uzZoxYtWlgdDgCgBmo55ZMyyxP99qiz/37td4ZoWdGFEtt/4P9kPnGF1SEAKENNzg3S0tJ0ySWX+PQaHy9hAABQjQSqRBf6/Sbp5KgkiSQA4Px99NFHHuemaSorK0svvPCC+vXr51ObJJMAAFQjLeyH5G+4dMAVrL2ucKvDAQDUEldddZXHuWEYioiI0KBBg/Tss8/61CbJJAAA1chOZxMdOh4su+ESo5IAgIricrkqvE2SSQAAqpkDZojEigYAgGqOZBIAgGrALpcCVKJjCrA6FABALWSapt555x2tXLlSOTk5pUYq33vvPa/btHSfSQAAcEJbe66uC9qirn6/Wh0KAKAWuueeezRmzBhlZGSofv36Cg8P9zh8wcgkAAAWM+RSZ79s2Q1ThSY/mgEAFe/111/Xe++9p+HDh1dYm4xMAgBgsdb231XfVqSjpp92OJtYHQ4AoBYKDw9Xq1atKrRNkkkAACxkyFQXvyxJ0k8l0XLyoxkAUAmmTZum6dOn69ixYxXWJnNpAACwUJz9oMJthSo07fq5JMLqcAAAtdR1112nxYsXKzIyUi1btpS/v7/H5xs3bvS6TZJJAAAs879Rya0lUSqR3eJ4AAC11S233KLU1FTddNNNioqKkmGc/17GJJMAAFgk3DiucKNQxaZNW0sirQ4HAFCLffLJJ/rss8/Uv3//CmuTZBIAAIscNoP19vHOamw7qiJ+JAMAKlFMTIzCwsIqtE3e8gcAwELH5a99Lt/29wIAoLyeffZZ3X///crMzKywNvkzKAAAFsjJybE6BABAHXLTTTfp6NGjat26terVq1dqAZ7ff//d6zZJJgEAqGJ79+7VggULlBQQppSitjJ1/osgAABwNrNnz67wNkkmAQCoYmvWrJEkHTX9SSQBAFXi5ptvrvA2SSYBAKhC+/fv17Zt2yRJm0uaWhwNAKCucDgcZ/08NjbW6zZJJgEAqEInRyU7duyoV74PsjgaAEBd0bJly7PuLel0Or1uk2QSAIAqcuDAAf3000+SdGKfr+9TLY4IAFBXpKWleZwXFxcrLS1Ns2bN0mOPPeZTmySTAABUkW+++Uamaapt27aKjo62OhwAQB3StWvXUmWJiYlq1qyZnn76aV1zzTVet8k+kwAAVAGn06ndu3dLkgYMGGBxNAAAnHDBBRfou+++8+laRiYBAKgCdrtdd9xxh3bt2qWYmBirwwEA1DF5eXke56ZpKisrS9OmTVPbtm19apNkEgCAKmK3233+gQ0AwPlo0KBBqQV4TNNUTEyM3nrrLZ/aJJkEAKCSZWVlKTIyUna73epQAAB11JdffumRTNpsNkVERKhNmzby8/MtLSSZBACgEh0/flyvvfaagoKCdMstt6hBgwZWhwQAqIMuvfTSCm+TBXgAAKhEGzZsUGFhoQICAhQeHm51OACAOmrmzJlauHBhqfKFCxfqySef9KlNRiYBAOXScsonVodQ4/jJqeuCtijIkN7ZV19PPbDM6pAAAHXUiy++qDfffLNUeceOHXX99dfrb3/7m9dtMjIJAEAlucD+m4KMEuW5ApXhbGR1OACAOiw7O1tNmzYtVR4REaGsrCyf2iSZBACgEtjkUif//ZKkzSXRMmWc4woAACpPTEyMvvnmm1Ll33zzjZo1a+ZTm0xzBQCgErSxH1CIUawC0187nY2tDgcAUMeNHz9eEydOVHFxsQYNGiRJ+uKLL3T//ffr3nvv9alNkkkAACpBhK1AkvRjcbRcTAQCAFjs/vvv1++//6477rhDRUVFkqSgoCD97W9/0wMPPOBTmySTAABUgm+KW2p7SRP9bgZbHQoAADIMQ08++aQefPBBpaenKzg4WG3btlVgYKDPbZJMAgBQSX4z61sdAgAAHurXr6+LLrqoQtpi3g0AABWooXFUQSq2OgwAACodI5MAAFQYU/0DMtXAOKaVRa2119XA6oAAAKg0jEwCAFBBmtny1MR2VKYM/eYKsTocAAAqFckkAAAVpKvfiU2ftzubqFD+FkcDAEDlIpkEAKACRNnyFW0/Iqdp6MfiaKvDAQCg0pFMAgBQAbr836jkL87GOqoAi6MBAKDysQAPAAA+MmQqypavSOOIWtjz5DKlzSVNrQ4LAIAqQTIJAIAP4mwH1cvfoRDb/7YBcclQY+Oojpi+bwANAEBNwTRXAAC8FGc7qIEBO1XP8NxP0i5TAwN2Ks520KLIAACoOiSTAAB4wZCpXv6OE18bp332f+c9/R0yZFZxZAAAVC2SSQAAvBBly1eIrbhUInmSYUj1bcWKsuVXbWAAAFQxy5PJOXPmKD4+XkFBQUpISNDq1avPWn/VqlVKSEhQUFCQWrVqpXnz5nl8/uqrr8owjFLH8ePHz6tfAAAkKfi0qa3nWw8AgJrK0mRyyZIlmjhxoqZOnaq0tDQNGDBAw4YNk8PhKLN+RkaGhg8frgEDBigtLU1///vfdffdd+vdd9/1qBcWFqasrCyPIygoyOd+AQA46ZjpX6H1AACoqSxNJmfNmqVx48Zp/Pjxat++vWbPnq2YmBjNnTu3zPrz5s1TbGysZs+erfbt22v8+PG67bbb9Mwzz3jUMwxD0dHRHsf59AsAwEn1jUKZZ3kd0jSlIy5/7XeFVl1QAABYwLJksqioSKmpqUpKSvIoT0pK0tq1a8u8Zt26daXqDxkyRN9//72Ki/83nejIkSOKi4tTixYtdOWVVyotLe28+pWkwsJC5eXluY/8fN6FAYC6xVQXvywNCNgtwziRNJ6eVJ4831AcK1NneKkSAIBawrJkMjc3V06nU1FRUR7lUVFRys7OLvOa7OzsMuuXlJQoNzdXknThhRfq1Vdf1UcffaTFixcrKChI/fr1044dO3zuV5Jmzpyp8PBw99GhQwev7xkAUHNF2Y4owX+fJGlLcZRWFrXS0dOmshaY/lpZ1Fq7XQ2tCBEAUMN4s47Le++9p8svv1wREREKCwtTnz599Nlnn1VhtKVZvgCPcdpyeKZplio7V/1Ty3v37q2bbrpJXbt21YABA7R06VJdcMEF+te//nVe/T7wwAM6fPiw+9i6deu5bw4AUGvsd4VqU3FTfVsUo+9LYrTb1UhvF3bRp4UX6KuieH1aeIHeKexCIgkAKBdv13H5+uuvdfnll2vZsmVKTU3VwIEDNWLECI9ZmFXNz6qOmzRpIrvdXmo0MCcnp9So4UnR0dFl1vfz81Pjxo3LvMZms+miiy5yj0z60q8kBQYGKjAw0H2el5d35psDANQKASqRJBX934/LtJLmHp+bMpTtCqvyuAAANd+p67hI0uzZs/XZZ59p7ty5mjlzZqn6s2fP9jh//PHH9eGHH+rjjz9W9+7dqyLkUiwbmQwICFBCQoJSUlI8ylNSUtS3b98yr+nTp0+p+itWrFBiYqL8/cteNc80TW3atElNmzb1uV8AQN0TYhRpeODPGhywQ3a5rA4HAFCL+LqOy6lcLpfy8/PVqFGjygixXCwbmZSk5ORkjRkzRomJierTp4/mz58vh8OhCRMmSDoxtXTfvn1atGiRJGnChAl64YUXlJycrNtvv13r1q3TggULtHjxYneb06dPV+/evdW2bVvl5eXp+eef16ZNm/Tvf/+73P0CAOq2BsYxJQVuV4hRrALTXyFGkfLMoHNfCACo0/Lz8z1mMJ4+u/EkX9dxOdWzzz6rgoICjRo16vyCPg+WJpOjR4/WgQMHNGPGDGVlZalTp05atmyZ4uLiJElZWVkec4bj4+O1bNkyTZo0Sf/+97/VrFkzPf/887r22mvddQ4dOqQ///nPys7OVnh4uLp3766vv/5aPXv2LHe/AIC6K8qWr8sCflGg4dQhV5BWFLVVgVn6FwEAAE53+iKdDz/8sKZNm3bG+t6u43LS4sWLNW3aNH344YeKjIz0KdaKYJjm2XbLwpns3btXMTEx2rNnj1q0aGF1OABQ6VpO+cTqECpdS9vvujggQ3bD1H5nfX1e1Mb9viRQHWQ+cYXVIQAow8ncYOvWrWre/H/v159pZLKoqEj16tXT22+/rauvvtpdfs8992jTpk1atWrVGftasmSJbr31Vr399tu64gpr/02wfDVXAACqgzb2XF0asEt2w9RuZwN9VnQBiSQAwCuhoaEKCwtzH2UlkpLv67gsXrxYt9xyi958803LE0nJ4mmuAABUFzmu+iqUnzJKGurb4liZOvc0IwAAfOXt+jGLFy/W2LFj9dxzz6l3797udyuDg4MVHh5uyT2QTAIA6jBT+r+kMc8M0ofHO+io/N1lAABUFm/Xj3nxxRdVUlKiO++8U3feeae7/Oabb9arr75a1eFLIpkEANRRfnLq0oBd2loSqV9dJ/6ie1QBFkcFAKhL7rjjDt1xxx1lfnZ6gvjVV19VfkBe4p1JAECdE6RiDQvcphj7YQ0IyGAfSQAAfMDIJACgTgkzjuvygB0KsxXquOmnLwrbyMnfVgEA8BrJJACgzmhiHNHlgb8oyChRnitQK4raKt8MsjosAABqJJJJAECd0Nx2WAMDdsrfcCnXVU8phW11XP5WhwUAQI1FMgkAqBPi7Aflb7i01xmmlUWtVSK71SEBAFCjkUwCAOqEdcWxOuQKUrozUibvSAIAcN74aQoAqBUMmYq25SnefkDRtjzZ5NIF9t9kyJQkmbJpqzOaRBIAgArCyCQAoMaLsx1UL3+HQmzF7rIS05CfYapRyVGtL46zMDoAAGonkkkAQI0WZzuogQE7S5X7GaZMUyoxGYkEAKAy8BMWAFBjGTLVy99x4muj7Drx9t/dU10BAEDFIZkEANRYUbZ8hdiKz5hIGoZU31asKFt+1QYGAEAdwDRXAKihWk75xOoQLBdsFJ+7khf1gOquqv+/z3ziiirtD0DNwsgkAKDGOmb6V2g9AABQfiSTAIAa65ArSAUuf5lneCXSNKUjLn/td4VWbWAAANQBJJMAgBrIVKLfHo0M2qofSpqeKDktoTx5vqE4VqbO8FIlAADwGckkAKBGscmli/0z1Nl/v+oZJTJlaGVRax09bSprgemvlUWttdvV0KJIAQCo3ViABwBQY/jJqUEBv6i5PV8u09Ca4pba6WwsSXIUNlCULV/BRrGOmSemtjIiCQBA5SGZBADUCMEq1uWBO9TYdlTFpk1fFrXWr65w9+emDGW7wiyMEACAuoVkEgBQ7dU3CjU0YJtCbUU6ZvoppbCtDpghVocFAECdRjIJAKj2jpt+Oi4/mS5DK4raKt8MsjokAADqPJJJAEC1VyK7Pi9sK0k6LvaMBACgOmA1VwBAtdTW/ps6+2W5z4/Ln0QSAIBqhJFJAEA1Y6qrX5Z6+P8qScpx1dd+V6jFMQEAgNORTAIAqg1Dpvr471Y7v1xJ0g/FTbXfVd/iqAAAQFlIJgEA1YJdTl0akKFY+yGZprSuOFbbnJFWhwUAAM6AZBIAYLlAlWhwwA5F2gtUYhpaVdRKDldDq8MCAABnQTIJALBcM3ueIu0FKjTt+ryojXJ4RxIAgGqPZBIAYLkMZyMFFxVrnytMh81gq8MBAADlwNYgAABLRNnyFahi9/lWZxSJJAAANQjJJACgysXbf9eQgO26PPAX+clpdTgAAMAHTHMFAFSpjn7Z6um/V5J0xBkgU4bFEQEAAF+QTAIAKoUhU1G2fAUbxTpm+mu/q74S/fapk/9+SdLWkkh9WxwjkUwCAFAjkUwCACpcnO2gevk7FGL73zuRJaYhP8OUJH1X3EI/lkSJRBIAgJqLZBIAUKHibAc1MGBnqXI/w5RpnhiR/LEk2oLIAABARWIBHgBAhTFkqpe/48TXZxh0jLMflCGzCqMCAACVgWQSAFBhomz5CrEVnzGRNAypvq1YUbb8qg0MAABUOJJJAECFCTaKz13Ji3oAAKD6IpkEAFSYY6Z/hdYDAADVF8kkAKDChBnHZZ7ldUjTlI64/LXfFVp1QQEAgEpheTI5Z84cxcfHKygoSAkJCVq9evVZ669atUoJCQkKCgpSq1atNG/ePI/PX3rpJQ0YMEANGzZUw4YNNXjwYG3YsMGjzrRp02QYhscRHc3KggDgO1Pd/PapX4BDhnEiaTw9qTx5vqE4ViZbggAAUONZmkwuWbJEEydO1NSpU5WWlqYBAwZo2LBhcjgcZdbPyMjQ8OHDNWDAAKWlpenvf/+77r77br377rvuOl999ZVuuOEGrVy5UuvWrVNsbKySkpK0b98+j7Y6duyorKws97Fly5ZKvVcAqK0Mmerrv1vd/bMkSZuKm2plUSsdPW0qa4Hpr5VFrbXb1dCKMAEAQAWzdJ/JWbNmady4cRo/frwkafbs2frss880d+5czZw5s1T9efPmKTY2VrNnz5YktW/fXt9//72eeeYZXXvttZKkN954w+Oal156Se+8846++OILjR071l3u5+fHaCQAVICTA5AuU1pfHKdtzghJkqOwoaJs+Qo2inXMPDG1lRFJAABqD8tGJouKipSamqqkpCSP8qSkJK1du7bMa9atW1eq/pAhQ/T999+ruLjslQGPHj2q4uJiNWrUyKN8x44datasmeLj43X99ddr165d53E3AFCXGVpXHKdPi9q5E0lJMmUo2xWmDGdjZbvCSCQBAKhlLEsmc3Nz5XQ6FRUV5VEeFRWl7OzsMq/Jzs4us35JSYlyc3PLvGbKlClq3ry5Bg8e7C7r1auXFi1apM8++0wvvfSSsrOz1bdvXx04cOCM8RYWFiovL8995OezRxqAuqu+Uaje/rtl/N+4pClDOSyqAwBAnWLpNFdJMk7b2do0zVJl56pfVrkkPfXUU1q8eLG++uorBQUFucuHDRvm/rpz587q06ePWrdurddee03Jycll9jtz5kxNnz793DcEALVcI+OoLg/crnpGiYpNu1JLWlgdEgAAsIBlI5NNmjSR3W4vNQqZk5NTavTxpOjo6DLr+/n5qXHjxh7lzzzzjB5//HGtWLFCXbp0OWssISEh6ty5s3bs2HHGOg888IAOHz7sPrZu3XrWNgGgNmpmO6zhgT+rnlGi313B2loSaXVIAADAIpYlkwEBAUpISFBKSopHeUpKivr27VvmNX369ClVf8WKFUpMTJS///9WDXz66af1yCOPaPny5UpMTDxnLIWFhUpPT1fTpk3PWCcwMFBhYWHuIzSU6VwA6pZW9gO6POAX+RsuZTlDtaywnY4pwOqwAACARSzdGiQ5OVkvv/yyFi5cqPT0dE2aNEkOh0MTJkyQdGI08NQVWCdMmKDdu3crOTlZ6enpWrhwoRYsWKDJkye76zz11FP6xz/+oYULF6ply5bKzs5Wdna2jhw54q4zefJkrVq1ShkZGfr222/1xz/+UXl5ebr55pur7uYBoMYw1ckvW5cEZMhmmNpV0lAritqq2Po3JQAAgIUs/U1g9OjROnDggGbMmKGsrCx16tRJy5YtU1xcnCQpKyvLY8/J+Ph4LVu2TJMmTdK///1vNWvWTM8//7x7WxBJmjNnjoqKivTHP/7Ro6+HH35Y06ZNkyTt3btXN9xwg3JzcxUREaHevXtr/fr17n4BAP8TYhSpm9+vkqQfS6L0XXELiZVZAQCo8wzz5Ao28MrevXsVExOjPXv2qEULFp8AUPVaTvmkyvpqbjusBrZj+qmE/XmBuiTziSusDgGoEepqbsAcJQBAKQEqUYhRpINmPUnSPle49rnCLY4KAABUJ5a+MwkAqH7qqUjDArdpaOB2hRnHrQ4HAABUU4xMAgDcwo1jSgrYofq2Ih01/WWXy+qQAABANUUyCQCQJEXa8jU44BcFGk4dcgUppaitjpiBVocFAACqKZJJAIBibQd1ScAu+Rmmclwh+rywjQrlf+4LAQBAnUUyCQB1XAvbIQ0M2CmbITmc4fqqqJWcslsdFoBqoCpXjZZYPRaoaUgmAaCOMGQqypavYKNYx0x/7XeFypShLFeocs0QHXQGa11xnEz2kAQAAOVAMgkAdUCc7aB6+TsUYit2lxW4/PVtcax2uxrqs8ILVCKbRCIJAADKia1BAKCWi7Md1MCAnapnFHuU1zOKNTBgp+JsB1Uiu0gkAQCAN0gmAaAWM2Sql7/jxNen5Yonz3v6O2TIrOLIAABATUcyCQC1WJQtXyG24lKJ5EmGIdW3FSvKll+1gQEAgBqPZBIAarHg06a2nm89AACAk0gmAaAWO26Wb521YyZ7SgIAAO+QTAJArWP+3yFlu8JUaNplnuGVSNOUjrhObBMCAADgDZJJAKhFGhpHNSxgm+Ltv0uSTBn6pijuxNenJZQnzzcUx7K3JAAA8Br7TAJALRCgEnX3/1UX2nNkM068A5nhbCTJ0G5XI60sMk7sM3nKu5EFpr82/N8+kwAAAN4imQSAGs1UG/sBJfrvVbBRIknKcDbUd8UtdOq+kbtdDeUobKAoW76CjWIdM09MbWVEEgAA+IpkEgBqqIbGUfX1361Ie4Ek6ZArSOuLY5XlCiuzvilD2Wf4DAAAwFskkwBQQwUaJYq0F6jYtGlTSTNtLYmUi1fhAQBAFSGZBIAawjRN7d+/X9HR0ZJOrNS6rihWDmcDHVWAxdEBAIC6hmQSAGqAffv2admyZfrtt9905513Kjw8XJL0szPS4sgAAEBdRTIJANVYQUGBvvjiC6WlpUmSAgMDlZOT404mAQAArEIyCQDVkMvlUmpqqr788ksdP35cktS1a1cNHjxY9evXtzg6AAAAksk6y+VyyeFwKD8/X6GhoYqNjZXNVrkLd1R1n/RXs/uzos/q0p/L5dLChQu1b98+SVJ0dLSGDRum2NjYSosFAADAWySTdVB6erqWL1+uvLw8d1lYWJiGDh2q9u3b14o+6a9m92dFn9Wtv/j4eB04cECDBg1SQkJCpSfuAACg6s2ZM0dPP/20srKy1LFjR82ePVsDBgw4Y/1Vq1YpOTlZP/30k5o1a6b7779fEyZMqMKIPfHbSR2Tnp6upUuXevwCK0l5eXlaunSp0tPTa3yf9Fez+7Oiz+rY34ABA3TXXXfpoosuIpEEAKAWWrJkiSZOnKipU6cqLS1NAwYM0LBhw+RwOMqsn5GRoeHDh2vAgAFKS0vT3//+d91999169913qzjy/2Fksg5xuVxavnz5Wet8/PHHcrlc7l9e4+PjFRQUJEn67bfflJube8Zr4+LiVK9ePUnSgQMHlJOTI5fLpU8++eSsfS5btsyjz9O1aNFCoaGhkqTDhw/r119/PWNb0dHR5b7H5s2bq0GDBpKkI0eOaM+ePWe8JioqSo0aNZIkHT16VLt375akct3f6d/TUzVp0kQRERGSpMLCQu3ateuM7TRq1EgRERHlur+wsDA1b95ckuR0OrV9+/Yz1j+1rsvl0rZt29yfnc/9hYSEeEzL3LZtm1wuV5ltBAcHq2XLlu4+//vf/561z+XLl6tdu3ay2Wz65ZdfVFxcXGa9gIAAtW7d2n2+a9cuFRYWetTx5R5tNpvatWvn/nz37t06evRomdcahqELL7zQo+7HH398zvu75557FBDAdh8AANRWs2bN0rhx4zR+/HhJ0uzZs/XZZ59p7ty5mjlzZqn68+bNU2xsrGbPni1Jat++vb7//ns988wzuvbaa6sydDeSyTrE4XCUGgk53bFjx/TOO++4zydMmOBOJrdu3aqvvvrqjNfedttt7mRy+/btWrFiRbniOnLkiEefp7v++uvdv7hnZmbqgw8+OGPdAQMGlPseR4wYoR49ekiSsrOztXTp0jNeM3ToUPXq1UvSiaT6bHXP1N+Z4h00aJAkKT8//6zt9u7dW+3atSvX/a1atUo33nijJKmoqOis7Xbp0kVXX321pBOJlTf3drK/su6vdevWuummm9zn7733noqKispsIzY2VrfeequkE8/pmRKzk/Ly8uRwONSyZUstW7ZMBw8eLLNe48aNddddd7nPP/vsM+Xk5Jzznk53+j0GBQXpb3/7m/t81apVysjIKPNau92uf/zjH+7zzz//XMeOHTtrf6feHwAAqDny8/M9flcLDAxUYGBgqXpFRUVKTU3VlClTPMqTkpK0du3aMttet26dkpKSPMqGDBmiBQsWqLi4WP7+/hVwB94hmaxD8vPzy1WvUaNGCgkJkSSPhzI8PFwxMTFnvO7U/1FCQ0MVExOjgoIC/f777171ebrg4GD31yEhIWeN4UwjX2X1d+qKmEFBQWdt99S6gYGB7rrne3+nbu/g7+9/1hgaNGhQ7v+Gp/63sNlsZ2335IirdGIU7dS653N/J0dcT2rRosUZRxAjI/+3V2J57/FkvaZNm55xddPTt89o2rRpqX/QfbnH09uIiIhQSUlJmdfZ7XaP81Of57Mp7/cBAABUHx06dPA4f/jhhzVt2rRS9XJzc+V0OhUVFeVRHhUVpezs7DLbzs7OLrN+SUmJcnNz1bRp0/ML3gckk3XIyami5zJixIgyR0S6deumbt26lauNTp06qVOnTsrMzNRrr73mc5+na9Omjdq0aXPGzzMzM/XNN9943V+LFi102223nfM66cRU2pN1K/L+wsPDzxlDZmZmuWJMSEhwfx0YGFjue7Pb7R51K/L+xowZU64Yyvucnqx33XXXlau+JF111VWlyiriHocNG1buGPr27asdO3acs155vw8AAKD62Lp1q/v1Ian0H6BPZxiGx7lpmqXKzlW/rPKqwqoOdUhsbKzCwsLOWicsLKxCtx+o6j7pr2b3Z0Wftb0/AABQdUJDQxUWFuY+zpRMNmnSRHa7vdQoZE5OTqnRx5Oio6PLrO/n56fGjRtXzA14iWSyDrHZbBo6dOhZ6wwdOrRCV46s6j7pr2b3Z0Wftb0/AABQ/QQEBCghIUEpKSke5SkpKerbt2+Z1/Tp06dU/RUrVigxMdGS9yUlksk6p3379ho1alSpkZGwsDCNGjWqUvbTq+o+6a9m92dFn7W9PwAAUP0kJyfr5Zdf1sKFC5Wenq5JkybJ4XC494184IEHNHbsWHf9CRMmaPfu3UpOTlZ6eroWLlyoBQsWaPLkyVbdggzz5ERbeGXv3r2KiYnRnj171KJFC6vD8ZrL5ZLD4VB+fr5CQ0MVGxtb6SMhVd0n/dXs/qzos6b113LK2bc0AYCaJvOJK6wOAfCJr7nBnDlz9NRTTykrK0udOnXSP//5T1188cWSpFtuuUWZmZkeuymsWrVKkyZN0k8//aRmzZrpb3/7mzv5tALJpI9qejIJoOYjmQRQ25BMoqaqq7kB01wBAAAAAF4jmQQAAAAAeI1kEgAAAADgNZJJAAAAAIDXSCYBAAAAAF4jmQQAAAAAeI1kEgAAAADgNZJJAAAAAIDXSCYBAAAAAF4jmQQAAAAAeM3yZHLOnDmKj49XUFCQEhIStHr16rPWX7VqlRISEhQUFKRWrVpp3rx5peq8++676tChgwIDA9WhQwe9//77590vAAAAAOB/LE0mlyxZookTJ2rq1KlKS0vTgAEDNGzYMDkcjjLrZ2RkaPjw4RowYIDS0tL097//XXfffbfeffddd51169Zp9OjRGjNmjH744QeNGTNGo0aN0rfffutzvwAAAAAAT4ZpmqZVnffq1Us9evTQ3Llz3WXt27fXVVddpZkzZ5aq/7e//U0fffSR0tPT3WUTJkzQDz/8oHXr1kmSRo8erby8PH366afuOkOHDlXDhg21ePFin/oty969exUTE6M9e/aoRYsW3t04AFSAllM+sToEAKhQmU9cYXUIgE/qam7gZ1XHRUVFSk1N1ZQpUzzKk5KStHbt2jKvWbdunZKSkjzKhgwZogULFqi4uFj+/v5at26dJk2aVKrO7Nmzfe5XkgoLC1VYWOg+P3z4sCQpKyvr7DcKAJWkJC/X6hAAoELt3bvX6hAAn5zMCVwul8WRVC3Lksnc3Fw5nU5FRUV5lEdFRSk7O7vMa7Kzs8usX1JSotzcXDVt2vSMdU626Uu/kjRz5kxNnz69VHnPnj3PfJMAAAAot5i5564DVGf79+9XbGys1WFUGcuSyZMMw/A4N02zVNm56p9eXp42ve33gQceUHJysvu8pKRE6enpiomJkc1m7TpG+fn56tChg7Zu3arQ0FBLY0HNwDMDb/HMwFs8M/AWzwy8VZ2eGZfLpf3796t79+6WxlHVLEsmmzRpIrvdXmo0MCcnp9So4UnR0dFl1vfz81Pjxo3PWudkm770K0mBgYEKDAz0KOvXr99Z7rDq5OXlSZKaN2+usLAwi6NBTcAzA2/xzMBbPDPwFs8MvFXdnpm6NCJ5kmVDagEBAUpISFBKSopHeUpKivr27VvmNX369ClVf8WKFUpMTJS/v/9Z65xs05d+AQAAAACeLJ3mmpycrDFjxigxMVF9+vTR/Pnz5XA4NGHCBEknppbu27dPixYtknRi5dYXXnhBycnJuv3227Vu3TotWLDAvUqrJN1zzz26+OKL9eSTT2rkyJH68MMP9fnnn2vNmjXl7hcAAAAAcHaWJpOjR4/WgQMHNGPGDGVlZalTp05atmyZ4uLiJJ1YFenUvR/j4+O1bNkyTZo0Sf/+97/VrFkzPf/887r22mvddfr27au33npL//jHP/Tggw+qdevWWrJkiXr16lXufmuawMBAPfzww6Wm4QJnwjMDb/HMwFs8M/AWzwy8xTNjPUv3mQQAAAAA1EzWLkMKAAAAAKiRSCYBAAAAAF4jmQQAAAAAeI1kEgAAAADgNZLJWmDOnDmKj49XUFCQEhIStHr1aqtDQjUwc+ZMXXTRRQoNDVVkZKSuuuoqbdu2zaOOaZqaNm2amjVrpuDgYF166aX66aefLIoY1c3MmTNlGIYmTpzoLuOZwen27dunm266SY0bN1a9evXUrVs3paamuj/nmcGpSkpK9I9//EPx8fEKDg5Wq1atNGPGDLlcLncdnpm67euvv9aIESPUrFkzGYahDz74wOPz8jwfhYWF+n//7/+pSZMmCgkJ0R/+8Aft3bu3Cu+i7iCZrOGWLFmiiRMnaurUqUpLS9OAAQM0bNgwjy1VUDetWrVKd955p9avX6+UlBSVlJQoKSlJBQUF7jpPPfWUZs2apRdeeEHfffedoqOjdfnllys/P9/CyFEdfPfdd5o/f766dOniUc4zg1MdPHhQ/fr1k7+/vz799FNt3bpVzz77rBo0aOCuwzODUz355JOaN2+eXnjhBaWnp+upp57S008/rX/961/uOjwzdVtBQYG6du2qF154oczPy/N8TJw4Ue+//77eeustrVmzRkeOHNGVV14pp9NZVbdRd5io0Xr27GlOmDDBo+zCCy80p0yZYlFEqK5ycnJMSeaqVatM0zRNl8tlRkdHm0888YS7zvHjx83w8HBz3rx5VoWJaiA/P99s27atmZKSYl5yySXmPffcY5omzwxK+9vf/mb279//jJ/zzOB0V1xxhXnbbbd5lF1zzTXmTTfdZJomzww8STLff/9993l5no9Dhw6Z/v7+5ltvveWus2/fPtNms5nLly+vstjrCkYma7CioiKlpqYqKSnJozwpKUlr1661KCpUV4cPH5YkNWrUSJKUkZGh7Oxsj+cnMDBQl1xyCc9PHXfnnXfqiiuu0ODBgz3KeWZwuo8++kiJiYm67rrrFBkZqe7du+ull15yf84zg9P1799fX3zxhbZv3y5J+uGHH7RmzRoNHz5cEs8Mzq48z0dqaqqKi4s96jRr1kydOnXiGaoEflYHAN/l5ubK6XQqKirKozwqKkrZ2dkWRYXqyDRNJScnq3///urUqZMkuZ+Rsp6f3bt3V3mMqB7eeustbdy4Ud99912pz3hmcLpdu3Zp7ty5Sk5O1t///ndt2LBBd999twIDAzV27FieGZTyt7/9TYcPH9aFF14ou90up9Opxx57TDfccIMk/p3B2ZXn+cjOzlZAQIAaNmxYqg6/H1c8kslawDAMj3PTNEuVoW676667tHnzZq1Zs6bUZzw/OGnPnj265557tGLFCgUFBZ2xHs8MTnK5XEpMTNTjjz8uSerevbt++uknzZ07V2PHjnXX45nBSUuWLNHrr7+uN998Ux07dtSmTZs0ceJENWvWTDfffLO7Hs8MzsaX54NnqHIwzbUGa9Kkiex2e6m/suTk5JT6iw3qrv/3//6fPvroI61cuVItWrRwl0dHR0sSzw/cUlNTlZOTo4SEBPn5+cnPz0+rVq3S888/Lz8/P/dzwTODk5o2baoOHTp4lLVv3969CBz/zuB09913n6ZMmaLrr79enTt31pgxYzRp0iTNnDlTEs8Mzq48z0d0dLSKiop08ODBM9ZBxSGZrMECAgKUkJCglJQUj/KUlBT17dvXoqhQXZimqbvuukvvvfeevvzyS8XHx3t8Hh8fr+joaI/np6ioSKtWreL5qaMuu+wybdmyRZs2bXIfiYmJ+tOf/qRNmzapVatWPDPw0K9fv1JbDm3fvl1xcXGS+HcGpR09elQ2m+evn3a73b01CM8MzqY8z0dCQoL8/f096mRlZenHH3/kGaoMli39gwrx1ltvmf7+/uaCBQvMrVu3mhMnTjRDQkLMzMxMq0ODxf7617+a4eHh5ldffWVmZWW5j6NHj7rrPPHEE2Z4eLj53nvvmVu2bDFvuOEGs2nTpmZeXp6FkaM6OXU1V9PkmYGnDRs2mH5+fuZjjz1m7tixw3zjjTfMevXqma+//rq7Ds8MTnXzzTebzZs3N//73/+aGRkZ5nvvvWc2adLEvP/++911eGbqtvz8fDMtLc1MS0szJZmzZs0y09LSzN27d5umWb7nY8KECWaLFi3Mzz//3Ny4caM5aNAgs2vXrmZJSYlVt1VrkUzWAv/+97/NuLg4MyAgwOzRo4d76wfUbZLKPF555RV3HZfLZT788MNmdHS0GRgYaF588cXmli1brAsa1c7pySTPDE738ccfm506dTIDAwPNCy+80Jw/f77H5zwzOFVeXp55zz33mLGxsWZQUJDZqlUrc+rUqWZhYaG7Ds9M3bZy5coyf3+5+eabTdMs3/Nx7Ngx86677jIbNWpkBgcHm1deeaXpcDgsuJvazzBN07RmTBQAAAAAUFPxziQAAAAAwGskkwAAAAAAr5FMAgAAAAC8RjIJAAAAAPAaySQAAAAAwGskkwAAAAAAr5FMAgAAAAC8RjIJAAAAAPAaySQAAAAAwGskkwAAVIHi4mKrQwAAoEKRTAIA6rR33nlHnTt3VnBwsBo3bqzBgweroKBAkrRw4UJ17NhRgYGBatq0qe666y73dQ6HQyNHjlT9+vUVFhamUaNGaf/+/e7Pp02bpm7dumnhwoVq1aqVAgMDZZqmDh8+rD//+c+KjIxUWFiYBg0apB9++KHK7xsAgPNFMgkAqLOysrJ0ww036LbbblN6erq++uorXXPNNTJNU3PnztWdd96pP//5z9qyZYs++ugjtWnTRpJkmqauuuoq/f7771q1apVSUlK0c+dOjR492qP9X375RUuXLtW7776rTZs2SZKuuOIKZWdna9myZUpNTVWPHj102WWX6ffff6/q2wcA4LwYpmmaVgcBAIAVNm7cqISEBGVmZiouLs7js+bNm+vWW2/Vo48+Wuq6lJQUDRs2TBkZGYqJiZEkbd26VR07dtSGDRt00UUXadq0aXr88ce1b98+RURESJK+/PJLXX311crJyVFgYKC7vTZt2uj+++/Xn//850q8WwAAKpaf1QEAAGCVrl276rLLLlPnzp01ZMgQJSUl6Y9//KOKi4v166+/6rLLLivzuvT0dMXExLgTSen/t3fHLqmFYQDGn1NtQQiJ1XTcQgeHqCEEI5DQzaGtrSkCtzYhWhskwX+kySE5EEGBQ3NTS0IETmVQQ1TDhQsRdfku13sv+PzGc3jPxzs+HPFAPp8nlUpxdXXFysoKAHEc/wxJgMvLSx4fH5mdnf3wvKenJ66vr0ewoSRJo2NMSpLG1uTkJN1ul4uLC05OTmi32zQaDZIk+Xbu7e2NKIp+eX16evrD/dfXVxYWFjg9Pf00m0qlfmsHSZL+FWNSkjTWoiiiWCxSLBbZ398njmO63S7ZbJYkSVhfX/80k8/nubm5od/vf/iZ6/39Pblc7suzlpaWuLu7Y2pqimw2O6qVJEn6K4xJSdLY6vV6JEnCxsYGmUyGXq/HYDAgl8txcHDAzs4OmUyGarXKcDjk/Pycer1OuVymUCiwtbVFq9Xi5eWF3d1d1tbWWF5e/vK8crnM6uoqtVqNw8NDFhcXub29pdPpUKvVvp2VJOl/Y0xKksbWzMwMZ2dntFotHh4eiOOYZrNJtVoF4Pn5maOjI/b29kin02xubgI/3mYeHx9Tr9cplUpMTExQqVRot9vfnhdFEZ1Oh0ajwfb2NoPBgPn5eUqlEnNzcyPfV5KkP8l/c5UkSZIkBfM7k5IkSZKkYMakJEmSJCmYMSlJkiRJCmZMSpIkSZKCGZOSJEmSpGDGpCRJkiQpmDEpSZIkSQpmTEqSJEmSghmTkiRJkqRgxqQkSZIkKZgxKUmSJEkKZkxKkiRJkoK9A0Or+WAR7UmhAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 1000x600 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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b968UuWRkZH685//TDIJAADK7bPPPlNsbKwuvPBC2Ww2tv8AgEpUr149/fnPf66w9rz+c9/u3bvLfHEzLi5ODoejQoICAAC13+7du7V+/Xq9/fbbOnjwoNXhAECt95///Ef9+/dXs2bNtHv3bknSP//5T3344Yc+ted1MhkZGanNmzeXKv/hhx/UuHFjn4IAAAB1i2maWrFihSSpR48eatSokcURAUDtNnfuXCUnJ2vYsGE6ePCgnE6nJKlhw4aaPXu2T216nUxef/31uvvuu7Vy5Uo5nU45nU59+eWXuueee3T99df7FAQAAKhbtmzZol9//VUBAQG69NJLrQ4HAGq9f/3rX3rppZc0depU+fn9723HxMREbdmyxac2vU4mH330UfXq1UuXXXaZgoODFRwcrKSkJA0aNEiPP/641wHMmTNH8fHxCgoKUkJCglavXn3GullZWbrxxhvVrl072Ww2TZw4sVSdl156SQMGDFDDhg3VsGFDDR48WBs2bPCoM23aNBmG4XFER0d7HTsAAPBecXGxvvjiC0lS//79Vb9+fYsjAoDaLyMjQ927dy9VHhgYqIKCAp/a9DqZDAgI0JIlS/Tzzz/rjTfe0HvvvaedO3dq4cKFCggI8KqtJUuWaOLEiZo6darS0tI0YMAADRs27IzvXhYWFioiIkJTp051L2d7uq+++ko33HCDVq5cqXXr1ik2NlZJSUnat2+fR72OHTsqKyvLffiajQMAAO+sX79eeXl5CgsLU+/eva0OBwDqhPj4eG3atKlU+aeffqoOHTr41KbP621fcMEFuu6663TllVcqLi7OpzZmzZqlcePGafz48Wrfvr1mz56tmJgYzZ07t8z6LVu21HPPPaexY8cqPDy8zDpvvPGG7rjjDnXr1k0XXnihXnrpJblcLvdfQE/y8/NTdHS0+4iIiPDpHgAAQPkdO3ZMa9askSRddtll8vf3tzgiALCON7M0pRODa1OnTlVcXJwCAwPVunVrLVy4sFx93Xfffbrzzju1ZMkSmaapDRs26LHHHtPf//533XfffT7F7/XWIE6nU6+++qq++OIL5eTkyOVyeXz+5ZdflqudoqIipaamasqUKR7lSUlJWrt2rbdhndHRo0dVXFxc6sX+HTt2qFmzZgoMDFSvXr30+OOPq1WrVhXWLwAAKC04OFjXXXedtmzZos6dO1sdDgBY5uQszTlz5qhfv3568cUXNWzYMG3dulWxsbFlXjNq1Cjt379fCxYsUJs2bZSTk6OSkpJy9XfrrbeqpKRE999/v44ePaobb7xRzZs313PPPefz2jdeJ5P33HOPXn31VV1xxRXq1KmTDMPwqePc3Fw5nU5FRUV5lEdFRSk7O9unNssyZcoUNW/eXIMHD3aX9erVS4sWLdIFF1yg/fv369FHH1Xfvn31008/nXFF2sLCQhUWFrrP8/PzKyxGAADqkjZt2qhNmzZWhwEAljp1lqYkzZ49W5999pnmzp2rmTNnlqq/fPlyrVq1Srt27XIPlJV3b96SkhK98cYbGjFihG6//Xbl5ubK5XIpMjLyvO7B62Tyrbfe0tKlSzV8+PDz6vik05NR0zR9TlBP99RTT2nx4sX66quvFBQU5C4fNmyY++vOnTurT58+at26tV577TUlJyeX2dbMmTM1ffr0CokLAIC66Pjx4x4/jwGgrvJlluZHH32kxMREPfXUU/rPf/6jkJAQ/eEPf9Ajjzyi4ODgs/bn5+env/71r0pPT5ckNWnSpELuw6cFeCrir4lNmjSR3W4vNQqZk5NTarTSF88884wef/xxrVixQl26dDlr3ZCQEHXu3Fk7duw4Y50HHnhAhw8fdh9bt2497xgBAKgrdu7cqdmzZ2vdunVWhwIAlSY/P195eXnu49SZjafyZZbmrl27tGbNGv344496//33NXv2bL3zzju68847yxVbr169lJaW5t0NnYPXyeS9996r5557TqZpnlfHAQEBSkhIUEpKikd5SkqK+vbte15tP/3003rkkUe0fPlyJSYmnrN+YWGh0tPT1bRp0zPWCQwMVFhYmPsIDQ09rxgBAKgrXC6XVqxYocLCQh0+fNjqcACg0nTo0EHh4eHuo6zpqqfyZpamy+WSYRh644031LNnTw0fPlyzZs3Sq6++qmPHjp0ztjvuuEP33nuvXnjhBa1bt06bN2/2OHzh9TTXNWvWaOXKlfr000/VsWPHUquwvffee+VuKzk5WWPGjFFiYqL69Omj+fPny+FwaMKECZJOjAbu27dPixYtcl9zcjnbI0eO6LffftOmTZsUEBDgXs72qaee0oMPPqg333xTLVu2dGf29evXd+9jNXnyZI0YMUKxsbHKycnRo48+qry8PN18883efjsAAMA5bNq0STk5OQoKCtIll1xidTgAUGm2bt2q5s2bu88DAwPLrOfLLM2mTZuqefPmHrtatG/fXqZpau/evWrbtu1ZYxs9erQk6e6773aXGYbhTmCdTufZb64MXieTDRo00NVXX+11R2UZPXq0Dhw4oBkzZigrK0udOnXSsmXL3FuNZGVlldpz8tSNNlNTU/Xmm28qLi5OmZmZkk4sr1tUVKQ//vGPHtc9/PDDmjZtmiRp7969uuGGG5Sbm6uIiAj17t1b69ev93mLEwAAULaioiKtXLlSknTxxRef870eAKjJQkNDFRYWds56p87SPDW3SklJ0ciRI8u8pl+/fnr77bd15MgR9yDZ9u3bZbPZ1KJFi3P2mZGRUc67KD+vk8lXXnmlQgO44447dMcdd5T52auvvlqq7FzTa08mlWfz1ltvlSc0AABwnr755hsdOXJEDRs21EUXXWR1OABQbXg7S/PGG2/UI488oltvvVXTp09Xbm6u7rvvPt12221n/ENdjx499MUXX6hhw4Z67bXXNHnyZNWrV6/C7sHrdyalE0vLfv7553rxxRfdW2T8+uuvOnLkSIUFBgAAara8vDz3qoSDBw+Wn5/Xf8MGgFpr9OjRmj17tmbMmKFu3brp66+/Pusszfr16yslJUWHDh1SYmKi/vSnP2nEiBF6/vnnz9hHenq6CgoKJEnTp0+v8HzN63/Vd+/eraFDh8rhcKiwsFCXX365QkND9dRTT+n48eOaN29ehQYIAABqpszMTDmdTsXExKh9+/ZWhwMA1Y63szQvvPDCUguYnk23bt106623qn///jJNU88884x7iuzpHnrooXK3e5LXyeQ999yjxMRE/fDDD2rcuLG7/Oqrr3ZvuAkAANClSxc1a9bMvQIhAKBqvfrqq3r44Yf13//+V4Zh6NNPPy1zlohhGFWTTK5Zs0bffPONAgICPMrj4uK0b98+rwMAAAC1V0VtjA0A8F67du3c68XYbDZ98cUXioyMrLD2vU4mXS5XmcvG7t27l70XAQCAIm1HVGz6tCwDAKCSuFyuCm/T62Ty8ssv1+zZszV//nxJJ4ZEjxw5oocffljDhw+v8AABAEDNYcilfv6ZCjOO65K/v67droZWhwQAqCReJ5P//Oc/NXDgQHXo0EHHjx/XjTfeqB07dqhJkyZavHhxZcQIAABqiHb2XDWwHdcx00+/us691xoAoObyOpls1qyZNm3apMWLF2vjxo1yuVwaN26c/vSnP7ERMQAAdViAStTd/1dJUlpxMxXLbnFEAIDK5NOGT8HBwbrtttt02223VXQ8AACghuril6Ugo0SHXEHa7oywOhwAQCXzOplctGjRWT8fO3asz8EAAICaqb5RqA5+OZKk74pbyBRbgQBAdXPo0CG988472rlzp+677z41atRIGzduVFRUlJo3b+51ez7tM3mq4uJiHT16VAEBAapXrx7JJAAAdVCC317ZDVO/OkO11xVudTgAgNNs3rxZgwcPVnh4uDIzM3X77berUaNGev/997V79+5zDhqWxet1uw8ePOhxHDlyRNu2bVP//v1ZgAcAgDrJVI6rvo6bftpQHCMxKgkA1U5ycrJuueUW7dixQ0FBQe7yYcOG6euvv/apTZ/emTxd27Zt9cQTT+imm27Szz//XBFNAgCAGsNQujNK250Rcnr/d2oAQBX47rvv9OKLL5Yqb968ubKzs31qs8L+xbfb7fr1118rqjkAAFDDkEgCQPUVFBSkvLy8UuXbtm1TRIRvi6Z5PTL50UcfeZybpqmsrCy98MIL6tevn09BAACAmscmly4L+EXbSiLkcDUQ01sBoPoaOXKkZsyYoaVLl0qSDMOQw+HQlClTdO211/rUptfJ5FVXXeVxbhiGIiIiNGjQID377LM+BQEAAGqeDn45amHPUyPbMe07HiYn+0oCQLX1zDPPaPjw4YqMjNSxY8d0ySWXKDs7W3369NFjjz3mU5teJ5Mul8unjgAAQO0RqGJ18cuSJKUWNyeRBIBqLiwsTGvWrNGXX36pjRs3yuVyqUePHho8eLDPbVbIAjwAAKBu6eafpUDDqQOuYO10NrY6HADAOWRmZqply5YaNGiQBg0aVCFtep1MJicnl7vurFmzvG0eAABUc2HGcV1o/02S9F1xjEzelQSAaq9Vq1bq27evxowZo+uuu06NGjU67za9TibT0tK0ceNGlZSUqF27dpKk7du3y263q0ePHu56hsEPFgAAaqNE/72yGab2OMOV5QqzOhwAQDl8//33Wrx4sR599FHdc889GjJkiG666Sb94Q9/UGBgoE9ter2G94gRI3TJJZdo79692rhxozZu3Kg9e/Zo4MCBuvLKK7Vy5UqtXLlSX375pU8BAQCA6quxUaA4+yG5TOm74hZWhwMAKKcePXro6aeflsPh0KeffqrIyEj95S9/UWRkpG677Taf2jRM0zS9uaB58+ZasWKFOnbs6FH+448/Kikpqc7sNbl3717FxMRoz549atGCH6YAAO+1nPKJ1SH4wFRzW54a2Y5qS0lTq4OxVOYTV1gdAoBqoqbmBhs3btS4ceO0efNmOZ1Or6/3emQyLy9P+/fvL1Wek5Oj/Px8rwMAAAA1iaF9rvA6n0gCQE21Z88ePfXUU+rWrZsuuugihYSE6IUXXvCpLa/fmbz66qt166236tlnn1Xv3r0lSevXr9d9992na665xqcgAABA9WaXU35yqVD+VocCAPDB/Pnz9cYbb+ibb75Ru3bt9Kc//UkffPCBWrZs6XObXieT8+bN0+TJk3XTTTepuLj4RCN+fho3bpyefvppnwMBAADViyFTUbZ8BRvFambLU5z9oL4rjtUOZxOrQwMAeOmRRx7R9ddfr+eee07dunWrkDa9Tibr1aunOXPm6Omnn9bOnTtlmqbatGmjkJCQCgkIAABYL852UL38HQqxFXuUNzCOWRQRAOB8OByOCt9xw+tk8qSsrCxlZWXp4osvVnBwsEzTZDsQAABqgTjbQQ0M2Fmq3DSljn77leOqr92uhhZEBgDwxubNm9WpUyfZbDZt2bLlrHW7dOnidfteJ5MHDhzQqFGjtHLlShmGoR07dqhVq1YaP368GjRooGeffdbrIAAAQPVgyFQvf8eJr0/7G7FhnEgoe/o75ChsIFP8ERkAqrNu3bopOztbkZGR6tatmwzD0KmbeZw8NwzDp9VcvU4mJ02aJH9/fzkcDrVv395dPnr0aE2aNIlkEgCAGizKll9qauupDEOqbxQrypavbFdYFUYGAPBWRkaGIiIi3F9XNK+TyRUrVuizzz4rtX9K27ZttXv37goLDAAAVL1g48yJpC/1AADWiYuLc3+9e/du9e3bV35+nilgSUmJ1q5d61G3vLzeZ7KgoED16tUrVZ6bm6vAwECvAwAAANXHMbN8W3+Utx4AoHoYOHCgfv/991Llhw8f1sCBA31q0+tk8uKLL9aiRYvc54ZhyOVy6emnn/Y5CAAAUD3sd4WqwOWvU16p8WCa0hGXv/a7Qqs2MADAeTnTgqkHDhzweWcOr6e5Pv3007r00kv1/fffq6ioSPfff79++ukn/f777/rmm298CgIAAFQPpgx9WxyrgQE7ZZqei/CcTDA3FMey+A4A1BDXXHONpBODgLfccovHbFKn06nNmzerb9++PrXtdTLZoUMHbd68WXPnzpXdbldBQYGuueYa3XnnnWratKlPQQAAgOpjt6uB1hXHqqtflkJOeTeywPTXhuJYtgUBgBokPDxc0omRydDQUAUHB7s/CwgIUO/evXX77bf71LZXyWRxcbGSkpL04osvavr06T51CAAAqrcWtsPq4+/QLmdDbS+OULBRrGPmiamtjEgCQM3yyiuvSJJatmypyZMn+zyltSxeJZP+/v768ccfy5xrCwAAaocL/X6TYUjHFMD2HwBQSzz88MMV3qbX01zHjh2rBQsW6IknnqjwYAAAgLVCjeNqYTssSdpWEmFxNACAivTOO+9o6dKlcjgcKioq8vhs48aNXrfndTJZVFSkl19+WSkpKUpMTCw1TDpr1iyvgwAAANXDhfYTo5J7nWHKM4OsDgcAUEGef/55TZ06VTfffLM+/PBD3Xrrrdq5c6e+++473XnnnT616XUy+eOPP6pHjx6SpO3bt3t8xvRXAABqLrucauuXK0lKL4m0OBoAQEWaM2eO5s+frxtuuEGvvfaa7r//frVq1UoPPfRQmftPlke5ksnNmzerU6dOstlsWrlypU8dAQCA6q2V/XcFGk7luwK0zxVudTgAgArkcDjcW4AEBwcrPz9fkjRmzBj17t1bL7zwgtdt2spTqXv37srNPfGXylatWunAgQNedwQAAKq31vYTf5n+2RnJqq0AUMtER0e787i4uDitX79ekpSRkSHz5EbCXipXMtmgQQNlZGRIkjIzM+VyuXzqDAAAVF+fF7XRN0Vx2lHSxOpQAAAVbNCgQfr4448lSePGjdOkSZN0+eWXa/To0br66qt9arNc01yvvfZaXXLJJWratKkMw1BiYqLsdnuZdXft2uVTIAAAwFolsmu7kxVcAaA2mj9/vntQcMKECWrUqJHWrFmjESNGaMKECT61Wa5kcv78+brmmmv0yy+/6O6779btt9+u0NBQnzoEAADVi00uuWRITG0FgFrLZrPJZvvfxNRRo0Zp1KhR59VmuVdzHTp0qCQpNTVV99xzD8kkAAC1RCe/bLWy/66Nxc3lcDW0OhwAQAXZvHlzuet26dLF6/bL9c7kqV555ZUKTSTnzJmj+Ph4BQUFKSEhQatXrz5j3aysLN14441q166dbDabJk6cWGa9d999Vx06dFBgYKA6dOig999//7z6BQCgtjJk6kL7b2poOy4/gzURAKA26datm7p3765u3bqd9ejevbtP7XudTFakJUuWaOLEiZo6darS0tI0YMAADRs2TA6Ho8z6hYWFioiI0NSpU9W1a9cy66xbt06jR4/WmDFj9MMPP2jMmDEaNWqUvv32W5/7BQCgtoq1HVKIrVjHTD9lOhmVBIDaJCMjQ7t27VJGRsZZD1/XvTFMX9eBrQC9evVSjx49NHfuXHdZ+/btddVVV2nmzJlnvfbSSy9Vt27dNHv2bI/y0aNHKy8vT59++qm7bOjQoWrYsKEWL1583v2etHfvXsXExGjPnj1q0aJFua4BAOBULad8YnUIGhKwTc3s+fqhOFobS/h55o3MJ66wOgQA1URdzQ0sG5ksKipSamqqkpKSPMqTkpK0du1an9tdt25dqTaHDBnibtPXfgsLC5WXl+c+Tm7yCQBATRVuHFMze75cprSNVVwBoNb7z3/+o379+qlZs2bavXu3JGn27Nn68MMPfWqv3AvwVLTc3Fw5nU5FRUV5lEdFRSk7O9vndrOzs8/apq/9zpw5U9OnT/c5LgAAqpv2fjmSpD2uBiowAy2OpuaxYmSZ0VAAvpo7d64eeughTZw4UY899picTqckqUGDBpo9e7ZGjhzpdZs+jUxWZEZrGJ7LkJumWaqsMtr0tt8HHnhAhw8fdh9bt249rxgBALCSn5xqbT8gSUovibQ4GgBAZfvXv/6ll156SVOnTpXdbneXJyYmasuWLT616XUyOXfuXCUnJ2v48OE6dOhQqYy2vJo0aSK73V5qNDAnJ6fUqKE3oqOjz9qmr/0GBgYqLCzMfbA1CgCgJiuRTSuLWiu9JEJZLn6mAUBtl5GRUeaqrYGBgSooKPCpTa+TyYrKaAMCApSQkKCUlBSP8pSUFPXt29fbsNz69OlTqs0VK1a426ysfgEAqFkM/eoK1/riOEnnNyMIAFD9xcfHa9OmTaXKP/30U3Xo0MGnNr1+Z7IiM9rk5GSNGTNGiYmJ6tOnj+bPny+Hw6EJEyZIOjG1dN++fVq0aJH7mpPfgCNHjui3337Tpk2bFBAQ4P4G3HPPPbr44ov15JNPauTIkfrwww/1+eefa82aNeXuFwAAAABqk/vuu0933nmnjh8/LtM0tWHDBi1evFgzZ87Uyy+/7FObXieTJzPauLg4j3JfMtrRo0frwIEDmjFjhrKystSpUyctW7bM3XZWVlapvR9PTWRTU1P15ptvKi4uTpmZmZKkvn376q233tI//vEPPfjgg2rdurWWLFmiXr16lbtfAABqs77+mSoy/fRTSaSOKcDqcAAAVeDWW29VSUmJ7r//fh09elQ33nijmjdvrueee07XX3+9T216vc/kK6+8ogcffFDPPvusxo0bp5dfflk7d+50Z7S+BlLT1NW9ZAAAFceK1UDrqUjXBW2WzZDeP95Rh8zgKo8BvmM1V6B6qu65QUlJid544w0NGTJE0dHRys3NlcvlUmTk+S3A5vXIZGVktAAAoGq08/tNNkPKctYnkQSAOsLPz09//etflZ6eLunEoqQV0q4vF91+++26/fbbKyyjBQAAlc8ml9r5/SaJ7UAAoK7p1auX0tLSKvTVPq+TyenTp+umm25S69atKyyjBQAAla+l/aCCjRIVmP5yuBpYHQ4AoArdcccduvfee7V3714lJCQoJCTE4/MuXbp43abXyeS7776rGTNm6KKLLtJNN92k0aNHKyIiwuuOAQBA1brQniNJ2lYSIdP73cEAADXY6NGjJUl33323u8wwDJmmKcMw5HQ6vW7T62Ry8+bN+umnn/TGG29o1qxZSk5O1uDBg3XTTTfpqquuUr169bwOAgAAVK5GxlFF2QvkNA1tL+GPwABQ12RkZFR4m16v5nq6b775Rm+++abefvttHT9+XHl5eRUVW7VW3VdsAgBUf1W5mmuIUahOfvtll0tri1tWWb+oWKzmClRPdTU38GkBnlOFhIQoODhYAQEBys/Pr4iYAABABSswA/VtcazVYQAAahGfXpjIyMjQY489pg4dOigxMVEbN27UtGnTlJ2dXdHxAQAAAACqIa9HJvv06aMNGzaoc+fOuvXWW937TAIAgOrIVG9/hzKcjbTfVV+SYXVAAIBawutkcuDAgXr55ZfVsWPHyogHAABUoBa2w2rv95ta2X/XkuNd5JTd6pAAALWE18nk448/XhlxAACASnCh32+SpB3OJiSSAFDHHTp0SO+884527typ++67T40aNdLGjRsVFRXl02zTciWTycnJeuSRRxQSEqLk5OSz1p01a5bXQQAAgIoXahxXC9thSSf2lgQA1F2bN2/W4MGDFR4erszMTN1+++1q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",
      "text/plain": [
       "<Figure size 1000x600 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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ffXV+u6779SrVy9fpwMAPlN+lebChQt1wQUX6JlnntHo0aO1Y8cOxcXFVfqe8ePH6+DBg1q6dKk6deqkvLw8lZWV1SjezTffrLKyMt1zzz06fvy4rrvuOrVr105PPvmkx2vfuF1M3nnnnXrhhRd02WWXqWfPnjIMw6PA+fn5stvtioqKcmmPiopSbm6uR2NWZubMmWrXrp1GjBjhbBs0aJCWL1+uLl266ODBg3rwwQc1ZMgQ/fDDD1WuSFtcXKzi4mLn88LCQq/lCABAU9KpUyd16tTJ12kAgE+dfpWmJC1YsEAffvihFi1apHnz5lXov2bNGn322Wfau3evc6KspnvzlpWV6eWXX9bYsWN16623Kj8/Xw6HQ5GRked0DG4Xk6+++qpWrVqlMWPGnFPgcmcWo6ZpelygnunRRx/VihUr9OmnnyooKMjZPnr0aOfXvXr1UnJysjp27KgXX3xRqamplY41b948zZkzxyt5AQDQFJ08edLl9zEANFWeXKX57rvvasCAAXr00Uf173//WyEhIfrd736nBx54QMHBwdXG8/Pz0//93/8pIyNDktSmTRuvHIdHC/B449PENm3ayGq1VpiFzMvLqzBb6YnHH39cDz/8sNauXavevXtX2zckJES9evXS7t27q+xz77336ujRo87Hjh07zjlHAACaij179mjBggXatGmTr1MBgFpTWFiogoIC5+P0KxtP58lVmnv37tX69ev1/fff66233tKCBQv0+uuv6/bbb69RboMGDVJ6erp7B3QWbheTd911l5588kmZpnlOgQMCApSUlKS0tDSX9rS0NA0ZMuScxn7sscf0wAMPaM2aNRowYMBZ+xcXFysjI0Nt27atsk9gYKDCwsKcj9DQ0HPKEQCApsLhcGjt2rUqLi7W0aNHfZ0OANSa7t27Kzw83Pmo7HLV07lzlabD4ZBhGHr55Zc1cOBAjRkzRvPnz9cLL7ygEydOnDW32267TXfddZeefvppbdq0Sdu3b3d5eMLty1zXr1+vdevW6YMPPlCPHj0qrML25ptv1nis1NRUTZw4UQMGDFBycrKWLFkim82mqVOnSjo1G3jgwAEtX77c+Z7y5WyPHTumX375Rdu2bVNAQIBzOdtHH31U9913n1555RUlJCQ4K/vmzZs797GaMWOGxo4dq7i4OOXl5enBBx9UQUGBbrzxRne/HQAA4Cy2bdumvLw8BQUF6aKLLvJ1OgBQa3bs2KF27do5nwcGBlbaz5OrNNu2bat27dq57GrRrVs3maap7Oxsde7cudrcJkyYIEm64447nG2GYTgLWLvdXv3BVcLtYrJFixa64oor3A5UmQkTJujQoUOaO3eucnJy1LNnT61evdq51UhOTk6FPSdP32hzy5YteuWVVxQfH6+srCxJp5bXLSkp0e9//3uX991///2aPXu2JCk7O1vXXnut8vPzFRERocGDB+vLL7/0eIsTAABQuZKSEq1bt06SdOGFF571vh4AaMhCQ0MVFhZ21n6nX6V5em2VlpamcePGVfqeCy64QK+99pqOHTvmnCTbtWuXLBaL2rdvf9aYmZmZNTyKmnO7mHz++ee9msBtt92m2267rdLXXnjhhQptZ7u8tryorM6rr75ak9QAAMA52rBhg44dO6aWLVvq/PPP93U6AFBvuHuV5nXXXacHHnhAN998s+bMmaP8/HzdfffduuWWW6r8oK5///76+OOP1bJlS7344ouaMWOGmjVr5rVjcPueSenU0rIfffSRnnnmGecWGT///LOOHTvmtcQAAEDDVlBQ4FyVcMSIEfLzc/szbABotCZMmKAFCxZo7ty56tu3rz7//PNqr9Js3ry50tLSdOTIEQ0YMEDXX3+9xo4dq6eeeqrKGBkZGSoqKpIkzZkzx+v1mts/1fft26dRo0bJZrOpuLhYl156qUJDQ/Xoo4/q5MmTWrx4sVcTBAAADVNWVpbsdrtiY2PVrVs3X6cDAPWOu1dpnnfeeRUWMK1O3759dfPNN2vo0KEyTVOPP/648xLZM/3tb3+r8bjl3C4m77zzTg0YMEDffvutWrdu7Wy/4oornBtuAgAA9O7dWzExMc4VCAEAdeuFF17Q/fffr//85z8yDEMffPBBpVeJGIZRN8Xk+vXrtWHDBgUEBLi0x8fH68CBA24nAAAAGi9vbYwNAHBf165dnevFWCwWffzxx4qMjPTa+G4Xkw6Ho9JlY7Ozs9l7EQAAKNJyTKWmR8syAABqicPh8PqYbheTl156qRYsWKAlS5ZIOjUleuzYMd1///0aM2aM1xMEAAANhyGHLvDPUphxUhf95SXtc7T0dUoAgFridjH5j3/8Q8OHD1f37t118uRJXXfdddq9e7fatGmjFStW1EaOAACggehqzVcLy0mdMP30s+Pse60BABout4vJmJgYbdu2TStWrNDWrVvlcDg0efJkXX/99WxEDABAExagMvXz/1mSlF4ao1JZfZwRAKA2ebThU3BwsG655Rbdcsst3s4HAAA0UL39chRklOmII0i77BG+TgcAUMvcLiaXL19e7euTJk3yOBkAANAwNTeK1d0vT5L0dWl7mWIrEACob44cOaLXX39de/bs0d13361WrVpp69atioqKUrt27dwez6N9Jk9XWlqq48ePKyAgQM2aNaOYBACgCUryy5bVMPWzPVTZjnBfpwMAOMP27ds1YsQIhYeHKysrS7feeqtatWqlt956S/v27TvrpGFl3F63+/Dhwy6PY8eOaefOnRo6dCgL8AAA0CSZynM010nTT5tLYyVmJQGg3klNTdVNN92k3bt3KygoyNk+evRoff755x6N6dE9k2fq3LmzHnnkEd1www368ccfvTEkAABoMAxl2KO0yx4hu/ufUwMA6sDXX3+tZ555pkJ7u3btlJub69GYXvuJb7Va9fPPP3trOAAA0MBQSAJA/RUUFKSCgoIK7Tt37lREhGeLprk9M/nuu++6PDdNUzk5OXr66ad1wQUXeJQEAABoeCxy6DcBP2lnWYRsjhbi8lYAqL/GjRunuXPnatWqVZIkwzBks9k0c+ZMXXXVVR6N6XYxefnll7s8NwxDERERuuSSS/TEE094lAQAAGh4uvvlqb21QK0sJ3TgZJjs7CsJAPXW448/rjFjxigyMlInTpzQRRddpNzcXCUnJ+uhhx7yaEy3i0mHw+FRIAAA0HgEqlS9/XIkSVtK21FIAkA9FxYWpvXr1+uTTz7R1q1b5XA41L9/f40YMcLjMb2yAA8AAGha+vrnKNCw65AjWHvsrX2dDgDgLLKyspSQkKBLLrlEl1xyiVfGdLuYTE1NrXHf+fPnuzs8AACo58KMkzrP+osk6evSWJncKwkA9V6HDh00ZMgQTZw4UVdffbVatWp1zmO6XUymp6dr69atKisrU9euXSVJu3btktVqVf/+/Z39DINfLAAANEYD/LNlMUztt4crxxHm63QAADXwzTffaMWKFXrwwQd15513auTIkbrhhhv0u9/9ToGBgR6N6fYa3mPHjtVFF12k7Oxsbd26VVu3btX+/fs1fPhw/fa3v9W6deu0bt06ffLJJx4lBAAA6q/WRpHirUfkMKWv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U2PGjNGwYcOUnp6uv/zlL7rjjjv0xhtv1HHm/8PMZBPicDi0Zs2aavu89957cjgczj9eExMTFRQUJEn65ZdflJ+fX+V74+Pj1axZM0nSoUOHlJeXJ4fDoffff7/amKtXr3aJeab27dsrNDRUknT06FH9/PPPVY4VHR1d42Ns166dWrRoIUk6duyY9u/fX+V7oqKi1KpVK0nS8ePHtW/fPkmq0fGd+T09XZs2bRQRESFJKi4u1t69e6scp1WrVoqIiKjR8YWFhaldu3aSJLvdrl27dlXZ//S+DodDO3fudL52LscXEhLiclnmzp075XA4Kh0jODhYCQkJzpj/+c9/qo25Zs0ade3aVRaLRT/99JNKS0sr7RcQEKCOHTs6n+/du1fFxcUufTw5RovFoq5duzpf37dvn44fP17pew3D0HnnnefS97333jvr8d15550KCGC7DwAAGqv58+dr8uTJmjJliiRpwYIF+vDDD7Vo0SLNmzevQv/FixcrLi5OCxYskCR169ZN33zzjR5//HFdddVVdZm6E8VkE2Kz2SrMhJzpxIkTev31153Pp06d6iwmd+zYoU8//bTK995yyy3OYnLXrl1au3ZtjfI6duyYS8wzXXPNNc4/3LOysvT2229X2XfYsGE1PsaxY8eqf//+kqTc3FytWrWqyveMGjVKgwYNknSqqK6ub1Xxqsr3kksukSQVFhZWO+7gwYPVtWvXGh3fZ599puuuu06SVFJSUu24vXv31hVXXCHpVGHlzrGVx6vs+Dp27KgbbrjB+fzNN99USUlJpWPExcXp5ptvlnTqPK2qMCtXUFAgm82mhIQErV69WocPH660X+vWrfWnP/3J+fzDDz9UXl7eWY/pTGceY1BQkP785z87n3/22WfKzMys9L1Wq1V//etfnc8/+ugjnThxotp4px8fAABoOAoLC13+VgsMDFRgYGCFfiUlJdqyZYtmzpzp0p6SkqKNGzdWOvamTZuUkpLi0jZy5EgtXbpUpaWl8vf398IRuIdisgkpLCysUb9WrVopJCREklxOyvDwcMXGxlb5vtP/o4SGhio2NlZFRUX69ddf3Yp5puDgYOfXISEh1eZQ1cxXZfFOXxEzKCio2nFP7xsYGOjse67Hd/r2Dv7+/tXm0KJFixr/G57+b2GxWKodt3zGVTo1i3Z633M5vvIZ13Lt27evcgYx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",
      "text/plain": [
       "<Figure size 1000x600 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig=plt.figure(figsize=(10,6))\n",
    "ax1=fig.add_subplot(111)\n",
    "ax2=ax1.twinx()\n",
    "weights=np.ones_like(english_scores)/len(english_scores)\n",
    "rel_freq,_,_=ax1.hist(english_scores,bins=25,\n",
    "                      range=(0,100),weights=weights)\n",
    "cum_rel_freq=np.cumsum(rel_freq)\n",
    "class_value=[(i+(i+4))//2 for i in range(0,100,4)]\n",
    "ax2.plot(class_value, cum_rel_freq,\n",
    "       ls='--',marker='o',color='gray')\n",
    "ax2.grid(visible=False)\n",
    "ax1.set_xlabel('score')\n",
    "ax1.set_ylabel('relative frequency')\n",
    "ax2.set_ylabel('cumulative relative frequency')\n",
    "ax1.set_xticks(np.linspace(0,100,25+1))\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "id": "baa9a68e-bd2f-41ad-95fd-3654dba47018",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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zooVK/LII4/k2WefTX19fe68887qsa9//et58MEH89BDD2XHjh25/PLL89hjj530/Z999tl84QtfyMqVK/Pcc8/l7/7u7/Kxj31s2DkbNmzIhRdemH/9139NT09PVq5cmS1btpz6k4exogKMyGuvvVa54IILKtu2bRu2/zd/8zcrt956a+Uf/uEfKkkqzzzzTPXY008/XUlSGRoaqlQqlcrMmTMrd99997Drr7/++sqHP/zh6s+333575ZOf/GT159mzZ1e++MUvViqVSuUv/uIvKuPGjav09/e/7YyzZ8+u3HDDDcP2ffSjH6186UtfqvXpwphlRQYj9MMf/jCvv/565s6dm4suuqi6PfHEE3nxxRer533oQx+q/nvChAlJkoMHDyZJnnvuufzyL//ysMd968//m7lz5+aKK67I5MmT8xu/8Rv5+te/nsHBwWHnvPn+x2c4fn/4eeDNHjBCx44dS5I8/fTT+cVf/MVhxxoaGqoxe/M7DI9/Wezxa9+877hKDR9/2tzcnJ07d+Y73/lONm/enPvvvz9dXV3Zvn17Lr744hPuf/x+b74/lM6KDEbogx/8YBoaGvLyyy/nl37pl4ZtHR0dJ/UYV111Vb773e8O2/fss8/WNEd9fX1uvPHG9PT05Pvf/37279+fv//7v6/pMaBkVmQwQs3NzbnnnnuydOnSHDt2LDfccEP6+/uzbdu2XHTRRbniiive9TF++7d/O3fddVeuu+66zJo1K9/85jfz/e9/P5MnTz6pGZ566qns3bs3H/vYx/K+970vf/M3f5Njx47lqquuOtWnB8UQMjgFf/AHf5BLL700q1atyt69e3PxxRdn+vTp+Z3f+Z2Tevnutttuy969e3PPPffk9ddfz2c/+9nccccdJ6zS3snFF1+cJ598Ml1dXXn99dfT2dmZb3zjG7n66qtP9alBMXwfGYwxc+fOTVtbW/70T/90tEeBIliRwSgaHBzM1772tfzqr/5qzjvvvHzjG9/IM8884++8oAZWZDCKhoaGcsstt2Tnzp05fPhwrrrqqtx3332ZP3/+aI8GxRAyAIrm7fcAFE3IACiakAFQNCEDoGhCBkDRhAyAogkZAEUTMgCK9v8BL75Pasdhb+QAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 500x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig=plt.figure(figsize=(5,6))\n",
    "ax=fig.add_subplot(111)\n",
    "ax.boxplot(english_scores, tick_labels=['english'])\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "id": "324f8a36-f93e-45b6-a2de-15d2138b1c35",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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AwCA2GIpuFy8eFGNjY3y+Xwh7T6fTydOnBhxTF5ens6dO6f6+noZY3T+/Hnt2bNHS5YsueJxBgYG1NfXF7IBAABYCi49PT0aGhqSx+MJafd4POrq6hpxTF5enmpra1VQUKCEhARNmzZNN998s958880rHqeiokJutzu4paenWykTAABEqYhuznU4HCH7xpiwtmEtLS0qLi7WSy+9pMbGRh06dEhnz55VUVHRFV+/rKxMgUAguHV0dERSJgAAiDJOK51TUlIUHx8ftrrS3d0dtgozrKKiQgsWLNDzzz8vSbr33ns1ZcoU5efn65VXXlFqamrYGJfLJZfLZaU0AAAQAyytuCQkJMjr9crv94e0+/1+5eXljTjmu+++U1xc6GHi4+MlXV6pAQAAuFaWLxWVlpbqvffeU01NjVpbW1VSUqL29vbgpZ+ysjIVFhYG+y9dulT79u1TVVWV2tradPz4cRUXF2v+/PlKS0sbvXcCAACinqVLRZJUUFCg3t5ebd68WZ2dnZozZ47q6+uVkZEhSers7Ax5psvq1avV39+vt956S3/4wx90880366GHHtKrr746eu8CAADEBIexwfWavr4+ud1uBQIBJSUlTXQ5AADgGozF+ZvfKgIAALZBcAEAALZBcAEAALZBcAEAALZBcAEAALZBcAEAALZBcAEAALZBcAEAALZBcAEAALZBcAEAALZBcAEAALZBcAEAALZBcAEAALZBcAEAALZBcAEAALZBcAEAALZBcAEAALZBcAEAALZBcAEAALZBcAEAALZBcAEAALZBcAEAALZBcAEAALYRUXCprKxUZmamEhMT5fV61dDQcNX+AwMDKi8vV0ZGhlwul+644w7V1NREVDAAAIhdTqsD6urqtG7dOlVWVmrBggV6++23tWjRIrW0tOi2224bcczy5ct1/vx5VVdX6xe/+IW6u7s1ODh43cUDAIDY4jDGGCsDcnJyNG/ePFVVVQXbsrKytGzZMlVUVIT1P3TokJ544gm1tbXplltuuaZjDAwMaGBgILjf19en9PR0BQIBJSUlWSkXAABMkL6+Prnd7lE9f1u6VHTx4kU1NjbK5/OFtPt8Pp04cWLEMQcPHlR2drZee+01TZ8+XbNnz9b69ev1/fffX/E4FRUVcrvdwS09Pd1KmQAAIEpZulTU09OjoaEheTyekHaPx6Ourq4Rx7S1tenYsWNKTEzU/v371dPTo2eeeUZff/31Fe9zKSsrU2lpaXB/eMUFAADENsv3uEiSw+EI2TfGhLUNu3TpkhwOh2pra+V2uyVJW7Zs0eOPP65t27Zp8uTJYWNcLpdcLlckpQEAgChm6VJRSkqK4uPjw1ZXuru7w1ZhhqWmpmr69OnB0CJdvifGGKNz585FUDIAAIhVloJLQkKCvF6v/H5/SLvf71deXt6IYxYsWKCvvvpK33zzTbDt9OnTiouL04wZMyIoGQAAxCrLz3EpLS3Ve++9p5qaGrW2tqqkpETt7e0qKiqSdPn+lMLCwmD/FStWKDk5WU8++aRaWlp09OhRPf/88/rd73434mUiAACAK7F8j0tBQYF6e3u1efNmdXZ2as6cOaqvr1dGRoYkqbOzU+3t7cH+P/vZz+T3+/X73/9e2dnZSk5O1vLly/XKK6+M3rsAAAAxwfJzXCbCWHwPHAAAjK0Jf44LAADARCK4AAAA2yC4AAAA2yC4AAAA2yC4AAAA2yC4AAAA2yC4AAAA2yC4AAAA2yC4AAAA2yC4AAAA2yC4AAAA2yC4AAAA2yC4AAAA2yC4AAAA2yC4AAAA2yC4AAAA2yC4AAAA2yC4AAAA2yC4AAAA2yC4AAAA2yC4AAAA2yC4AAAA24gouFRWViozM1OJiYnyer1qaGi4pnHHjx+X0+nUfffdF8lhAQBAjLMcXOrq6rRu3TqVl5erqalJ+fn5WrRokdrb2686LhAIqLCwUL/5zW8iLhYAAMQ2hzHGWBmQk5OjefPmqaqqKtiWlZWlZcuWqaKi4orjnnjiCc2aNUvx8fE6cOCAmpubr/mYfX19crvdCgQCSkpKslIuAACYIGNx/ra04nLx4kU1NjbK5/OFtPt8Pp04ceKK43bs2KEzZ85o48aN13ScgYEB9fX1hWwAAACWgktPT4+Ghobk8XhC2j0ej7q6ukYc89lnn2nDhg2qra2V0+m8puNUVFTI7XYHt/T0dCtlAgCAKBXRzbkOhyNk3xgT1iZJQ0NDWrFihTZt2qTZs2df8+uXlZUpEAgEt46OjkjKBAAAUebalkD+fykpKYqPjw9bXenu7g5bhZGk/v5+nTp1Sk1NTXruueckSZcuXZIxRk6nU4cPH9ZDDz0UNs7lcsnlclkpDQAAxABLKy4JCQnyer3y+/0h7X6/X3l5eWH9k5KS9Mknn6i5uTm4FRUV6c4771Rzc7NycnKur3oAABBTLK24SFJpaalWrlyp7Oxs5ebm6p133lF7e7uKiookXb7M8+WXX+r9999XXFyc5syZEzJ+6tSpSkxMDGsHAAD4KZaDS0FBgXp7e7V582Z1dnZqzpw5qq+vV0ZGhiSps7PzJ5/pAgAAEAnLz3GZCDzHBQAA+5nw57gAAABMJIILAACwDYILAACwDYILAACwDYILAACwDYILAACwDYILAACwDYILAACwDYILAACwDYILAACwDYILAACwDYILAACwDYILAACwDYILAACwDYILAACwDYILAACwDYILAACwDYILAACwDYILAACwDYILAACwDYILAACwDYILAACwDYILAACwjYiCS2VlpTIzM5WYmCiv16uGhoYr9t23b58efvhh3XrrrUpKSlJubq4+/PDDiAsGAACxy3Jwqaur07p161ReXq6mpibl5+dr0aJFam9vH7H/0aNH9fDDD6u+vl6NjY168MEHtXTpUjU1NV138QAAILY4jDHGyoCcnBzNmzdPVVVVwbasrCwtW7ZMFRUV1/Qa99xzjwoKCvTSSy9dU/++vj653W4FAgElJSVZKRcAAEyQsTh/W1pxuXjxohobG+Xz+ULafT6fTpw4cU2vcenSJfX39+uWW265Yp+BgQH19fWFbAAAAJaCS09Pj4aGhuTxeELaPR6Purq6ruk1Xn/9dX377bdavnz5FftUVFTI7XYHt/T0dCtlAgCAKBXRzbkOhyNk3xgT1jaS3bt36+WXX1ZdXZ2mTp16xX5lZWUKBALBraOjI5IyAQBAlHFa6ZySkqL4+Piw1ZXu7u6wVZgfq6ur05o1a/TBBx9o4cKFV+3rcrnkcrmslAYAAGKApRWXhIQEeb1e+f3+kHa/36+8vLwrjtu9e7dWr16tXbt2acmSJZFVCgAAYp6lFRdJKi0t1cqVK5Wdna3c3Fy98847am9vV1FRkaTLl3m+/PJLvf/++5Iuh5bCwkK98cYbuv/++4OrNZMnT5bb7R7FtwIAAKKd5eBSUFCg3t5ebd68WZ2dnZozZ47q6+uVkZEhSers7Ax5psvbb7+twcFBPfvss3r22WeD7atWrdLOnTuv/x0AAICYYfk5LhOB57gAAGA/E/4cFwAAgIlEcAEAALZBcAEAALZBcAEAALZBcAEAALZBcAEAALZBcAEAALZBcAEAALZBcAEAALZBcAEAALZBcAEAALZBcAEAALZBcAEAALZBcAEAALZBcAEAALZBcAEAALZBcAEAALZBcAEAALZBcAEAALZBcAEAALZBcAEAALZBcAEAALZBcAEAALYRUXCprKxUZmamEhMT5fV61dDQcNX+R44ckdfrVWJiombOnKnt27dHVCwAAIhtloNLXV2d1q1bp/LycjU1NSk/P1+LFi1Se3v7iP3Pnj2rxYsXKz8/X01NTXrxxRdVXFysvXv3XnfxAAAgtjiMMcbKgJycHM2bN09VVVXBtqysLC1btkwVFRVh/V944QUdPHhQra2twbaioiJ9/PHHOnny5IjHGBgY0MDAQHA/EAjotttuU0dHh5KSkqyUCwAAJkhfX5/S09N14cIFud3u0XlRY8HAwICJj483+/btC2kvLi42v/71r0cck5+fb4qLi0Pa9u3bZ5xOp7l48eKIYzZu3GgksbGxsbGxsUXBdubMGStx46qcsqCnp0dDQ0PyeDwh7R6PR11dXSOO6erqGrH/4OCgenp6lJqaGjamrKxMpaWlwf0LFy4oIyND7e3to5fYEJHh9Mzq18RjLm4czMWNhfm4cQxfMbnllltG7TUtBZdhDocjZN8YE9b2U/1Hah/mcrnkcrnC2t1uN/8T3iCSkpKYixsEc3HjYC5uLMzHjSMubvS+xGzplVJSUhQfHx+2utLd3R22qjJs2rRpI/Z3Op1KTk62WC4AAIhlloJLQkKCvF6v/H5/SLvf71deXt6IY3Jzc8P6Hz58WNnZ2Zo0aZLFcgEAQCyzvHZTWlqq9957TzU1NWptbVVJSYna29tVVFQk6fL9KYWFhcH+RUVF+uKLL1RaWqrW1lbV1NSourpa69evv+Zjulwubdy4ccTLRxhfzMWNg7m4cTAXNxbm48YxFnNh+evQ0uUH0L322mvq7OzUnDlz9H//93/69a9/LUlavXq1Pv/8c3300UfB/keOHFFJSYk+/fRTpaWl6YUXXggGHQAAgGsVUXABAACYCPxWEQAAsA2CCwAAsA2CCwAAsA2CCwAAsI0bJrhUVlYqMzNTiYmJ8nq9amhouGr/I0eOyOv1KjExUTNnztT27dvHqdLoZ2Uu9u3bp4cffli33nqrkpKSlJubqw8//HAcq41uVj8Xw44fPy6n06n77rtvbAuMIVbnYmBgQOXl5crIyJDL5dIdd9yhmpqacao2ulmdi9raWs2dO1c33XSTUlNT9eSTT6q3t3ecqo1eR48e1dKlS5WWliaHw6EDBw785JhROXeP2q8eXYe//vWvZtKkSebdd981LS0tZu3atWbKlCnmiy++GLF/W1ubuemmm8zatWtNS0uLeffdd82kSZPMnj17xrny6GN1LtauXWteffVV869//cucPn3alJWVmUmTJpn//Oc/41x59LE6F8MuXLhgZs6caXw+n5k7d+74FBvlIpmLRx991OTk5Bi/32/Onj1r/vnPf5rjx4+PY9XRyepcNDQ0mLi4OPPGG2+YtrY209DQYO655x6zbNmyca48+tTX15vy8nKzd+9eI8ns37//qv1H69x9QwSX+fPnm6KiopC2u+66y2zYsGHE/n/84x/NXXfdFdL29NNPm/vvv3/MaowVVudiJHfffbfZtGnTaJcWcyKdi4KCAvOnP/3JbNy4keAySqzOxd/+9jfjdrtNb2/veJQXU6zOxZ///Gczc+bMkLatW7eaGTNmjFmNsehagstonbsn/FLRxYsX1djYKJ/PF9Lu8/l04sSJEcecPHkyrP8jjzyiU6dO6YcffhizWqNdJHPxY5cuXVJ/f/+o/hJoLIp0Lnbs2KEzZ85o48aNY11izIhkLg4ePKjs7Gy99tprmj59umbPnq3169fr+++/H4+So1Ykc5GXl6dz586pvr5exhidP39ee/bs0ZIlS8ajZPyP0Tp3R/Tr0KOpp6dHQ0NDYT/S6PF4wn6ccVhXV9eI/QcHB9XT06PU1NQxqzeaRTIXP/b666/r22+/1fLly8eixJgRyVx89tln2rBhgxoaGuR0TvhHO2pEMhdtbW06duyYEhMTtX//fvX09OiZZ57R119/zX0u1yGSucjLy1Ntba0KCgr03//+V4ODg3r00Uf15ptvjkfJ+B+jde6e8BWXYQ6HI2TfGBPW9lP9R2qHdVbnYtju3bv18ssvq66uTlOnTh2r8mLKtc7F0NCQVqxYoU2bNmn27NnjVV5MsfK5uHTpkhwOh2prazV//nwtXrxYW7Zs0c6dO1l1GQVW5qKlpUXFxcV66aWX1NjYqEOHDuns2bP87MwEGY1z94T/sywlJUXx8fFhabm7uzssmQ2bNm3aiP2dTqeSk5PHrNZoF8lcDKurq9OaNWv0wQcfaOHChWNZZkywOhf9/f06deqUmpqa9Nxzz0m6fPI0xsjpdOrw4cN66KGHxqX2aBPJ5yI1NVXTp0+X2+0OtmVlZckYo3PnzmnWrFljWnO0imQuKioqtGDBAj3//POSpHvvvVdTpkxRfn6+XnnlFVbox9FonbsnfMUlISFBXq9Xfr8/pN3v9ysvL2/EMbm5uWH9Dx8+rOzsbE2aNGnMao12kcyFdHmlZfXq1dq1axfXjUeJ1blISkrSJ598oubm5uBWVFSkO++8U83NzcrJyRmv0qNOJJ+LBQsW6KuvvtI333wTbDt9+rTi4uI0Y8aMMa03mkUyF999953i4kJPdfHx8ZL+37/2MT5G7dxt6VbeMTL89bbq6mrT0tJi1q1bZ6ZMmWI+//xzY4wxGzZsMCtXrgz2H/5KVUlJiWlpaTHV1dV8HXqUWJ2LXbt2GafTabZt22Y6OzuD24ULFybqLUQNq3PxY3yraPRYnYv+/n4zY8YM8/jjj5tPP/3UHDlyxMyaNcs89dRTE/UWoobVudixY4dxOp2msrLSnDlzxhw7dsxkZ2eb+fPnT9RbiBr9/f2mqanJNDU1GUlmy5YtpqmpKfjV9LE6d98QwcUYY7Zt22YyMjJMQkKCmTdvnjly5Ejwz1atWmUeeOCBkP4fffSR+eUvf2kSEhLM7bffbqqqqsa54uhlZS4eeOABIylsW7Vq1fgXHoWsfi7+F8FldFmdi9bWVrNw4UIzefJkM2PGDFNaWmq+++67ca46Olmdi61bt5q7777bTJ482aSmpprf/va35ty5c+NcdfT5+9//ftW//8fq3O0whrUyAABgDxN+jwsAAMC1IrgAAADbILgAAADbILgAAADbILgAAADbILgAAADbILgAAADbILgAAADbILgAAADbILgAAADbILgAAADb+P8Axh+er5h8KfwAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 640x480 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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oVDYvRZCNGmjOzNjxgz88MMPyM7ObnKO4353ioqKMHv2bOzevRve3t43jOM43z2bzYaBAwciJSUFADBgwAAcP34c69evx4svvijHcazvzscff4wtW7Zg27Zt6N+/P/Ly8pCcnAydToeJEyfKcRznlnEn4+rIsefUVQsIDg6Gu7t7k2y0rKysSWZLt2/mzJnYsWMH9u7di+7du8vtWq0WADjudyk3NxdlZWWIioqCh4cHPDw8kJWVhbfffhseHh7yWHKc717Xrl3Rr18/u7a+ffvi/PnzAPgz7Sh//vOfsXDhQjz33HOIjIxEUlISXn31VaSmpgLgOLeU5oyrVquFxWKBwWC4YczdYqLTAry8vBAVFYXMzEy79szMTMTGxjqpV+2fEAIzZszAp59+iq+++gqhoaF250NDQ6HVau3G3WKxICsri+N+G0aOHIljx44hLy9PPgYOHIgXXngBeXl5CAsL4zg7yJAhQ5pskXDmzBn5wcT8mXaM6upquLnZ/7pzd3eXl5dznFtGc8Y1KioKnp6edjGlpaXIz8933Ng75JZmauLa8vL33ntPnDhxQiQnJws/Pz/x888/O7tr7dbLL78sJEkSX3/9tSgtLZWP6upqOebNN98UkiSJTz/9VBw7dkw8//zzXCLqAL9ddSUEx9lRcnJyhIeHh1i+fLn48ccfxdatW4Wvr6/YsmWLHMOxvnsTJ04U3bp1k5eXf/rppyI4OFjMnz9fjuE435nKykpx5MgRceTIEQFArFq1Shw5ckTeSqU54zpt2jTRvXt3sWfPHnH48GHxu9/9jsvL24t33nlH9OzZU3h5eYmHHnpIXgZNdwbAdY/3339fjrHZbOL1118XWq1WKJVKMWzYMHHs2DHnddpFNE50OM6Os3PnThERESGUSqXo06eP2Lhxo915jvXdM5lMYvbs2aJHjx7C29tbhIWFicWLFwuz2SzHcJzvzN69e6/77/LEiROFEM0b15qaGjFjxgwRGBgofHx8RHx8vDh//rzD+qgQQgjH1IaIiIiI2hbeo0NEREQui4kOERERuSwmOkREROSymOgQERGRy2KiQ0RERC6LiQ4RERG5LCY6RERE5LKY6BAREZHLYqJDRERELouJDhEREbksJjpERETkspjoEBERkcv6/wEIDGu8Uscb7QAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 640x480 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "fig=plt.figure()\n",
    "ax1=fig.add_subplot(2,1,1)\n",
    "ax2=fig.add_subplot(2,1,2)\n",
    "x=range(0,100)\n",
    "y=[v*v for v in x ]\n",
    "ax1.plot(x,y)\n",
    "ax2.bar(x,y)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "371d1d36-6717-4eaf-a1bf-259b0c0ab213",
   "metadata": {},
   "outputs": [],
   "source": [
    "ax"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
