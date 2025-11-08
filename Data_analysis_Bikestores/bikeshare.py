import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def input_cheacker(input_str,input_type):
    while True: 
        input_read=input(input_str).casefold()
        try:
            if input_read in ['chicago','new york city','washington'] and input_type==1:
                break
            elif input_read in ['january','february','march','april','all'] and input_type==2:
                break
            elif input_read in ['friday','satuerday','sunday','monday','tuesday','wednesday','thursday',"all"] and input_type==3:
                break
            else :
                if input_type==1:
                    print("you enter wrong city ")
                if input_type==2:
                    print("you enter wrong month ")
                if input_type==3:
                    print("you enter wrong day")
        except ValueError :
            print("you enter wrong input")
    return input_read
            
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input_cheacker('what is city do you want (chicago,New york or Washington) ?? ',1)

    # TO DO: get user input for month (all, january, february, ... , june)
    month=input_cheacker("which month do you want ??  (Note: please write it in letters not as numbers)  ",2)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input_cheacker("which day do you want ??   ",3)

    print('-'*40)
    return city,month, day



def load_data(city,month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.strftime('%A')
    df['hour']= df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new 
        df = df[df['day_of_week'] == day.title()]

    return df
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_months=df['month'].mode()[0]
    print("the most common months is ",most_common_months)   
    # TO DO: display the most common day of week
    most_common_days=df['day_of_week'].mode()[0]
    print("the most common days is ",most_common_days)


    # TO DO: display the most common start hour
    most_common_hours= df['hour'].mode()[0]
    print("the most common hours is  ",most_common_hours)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_Startstation=df['Start Station'].mode()[0]
    print("the most common start station is ",most_common_Startstation)

    # TO DO: display most commonly used end station
    most_common_endstation=df['End Station'].mode()[0]
    print("the most common start station is ",most_common_endstation)
    # TO DO: display most frequent combination of start station and end station trip
    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most commonly used start station and end station : {}, {}"\
            .format(most_common_start_end_station[0], most_common_start_end_station[1]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tota_travel_time= df["Trip Duration"].sum()
    print("the total time travel is ",tota_travel_time)

    # TO DO: display mean travel time
    average_travel_time= df["Trip Duration"].mean()
    print("the average of travel time ",average_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_usertypes=df['User Type'].value_counts()
    print("the counts of user types : ",counts_of_usertypes)
    # TO DO: Display counts of gender
    if city != 'washington':
        print("the counts of genders is " , df['Gender'].value_counts())
        print("the most common year of birth is " , df['Birth Year'].mode()[0])
        print("the maxmium of years of birth is " , df['Birth Year'].max())
        print("the minumum of years of birth is " , df['Birth Year'].min())
    else:
        print("this data not found in washinghton")

 # TO DO: Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
