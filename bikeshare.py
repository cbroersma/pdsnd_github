import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_city():
    """
    Asks user to specify a city to analyze.

    Returns:
        (str) city - name of the city to analyze
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). While loop to handle invalid inputs
    city = input("Enter which city's bikeshare data you would like to investigate.\n  Chicago, New York City, or Washington: ")
    city = city.lower()
    while True:
            if city == 'chicago':
                print("The 'Windy City'...Let's go!")
                print('-'*40)
                return 'chicago'
            if city == 'new york city':
                print("The City that Never Sleeps...Let's go!")
                print('-'*40)

                return 'new york city'
            if city == 'washington':
                print("The Nation's capital...Let's go!")
                print('-'*40)
                return 'washington'
            else:
                print('Please enter either Chicago, New York City, or Washington...')
                city = input("Enter which city's bikeshare data you would like investigate: ")
                city = city.lower()
    return city
def get_time_filter():
    """
    Asks user to specify a month and day to filter by.

    Returns:
        (str) month - name of the month to filter by
        (str) day - name of day to filter by
    """
    accepted_months = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6}
    month = ''
    #while loop to handle invalid inputs
    # get user input for month (january, february, ... , june)
    while month not in accepted_months:
        month = input("Which month would you like to take a look at, January, February, March, April, May, or June?:\n").lower()
        if month not in accepted_months:
            print('Please enter the full name of a month between January and June...')
    print("filtering by month...")
    print('-'*40)

    # get user input for day of week (monday, tuesday, ... sunday)
    accepted_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday', 'Satureday', 'Sunday']
    day = ''
    while day not in accepted_days:
        day = input('Which day would you like to filter by? Please type a day... Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday: \n').title()
        if day not in accepted_days:
            print('Invalid input...')
    print('filtering by day...')
    return month, day





    print('-'*40)


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by
        (str) day - name of the day of week to filter by
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #read csv for specified city
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #extract month from start time
    df['month'] = df['Start Time'].dt.month

    #extract day of week from start time
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month
    # use the index of the months list to get the corresponding int
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month = months.index(month) + 1

    # filter by month to create the new dataframe
    df = df[df['month'] == month]

    # filter by day of week
    # filter by day of week to create the new dataframe
    df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):

    """Displays statistics on the most frequent times of travel."""


    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]


    print("Most Popular Month: ", popular_month)

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]

    print("Most Popular Day of the Week: ", popular_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):

    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_start_station)


    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_end_station)


    # display most frequent combination of start station and end station trip
    # combine start and end station to show total trip in 'Start to End' column
    df['Start to End'] = df['Start Station'] + ' to ' + df['End Station']
    trip_start_to_end = df['Start to End'].mode()[0]
    print('The most common trip is from ', trip_start_to_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):

    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    #convert time to hour, minute, second format
    minute, second = divmod(total_travel_time, 60)
    hour, minute = divmod(minute, 60)
    print('Total Travel Time is ', hour, 'hour(s)', minute, 'minutes', round(second), 'seconds')
    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    mean_minute, mean_second = divmod(mean_travel_time, 60)
    #if mean time is greater than 60 minutes convert to hour, minute, second format
    #if not show in minute, second format
    if mean_minute > 60:
        mean_hour, mean_minute = divmod(mean_minute, 60)
        print('Average Travel Time is ', mean_hour, 'hour(s)',
        mean_minute, 'minutes', round(mean_second), 'seconds')
    elif mean_minute < 60:
        print('Average Travel Time is ', mean_minute, 'minutes', round(mean_second), 'seconds')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):

    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df['User Type'].value_counts()
    print(f'The type of users by number are: \n{user_type}')

    # Display counts of gender
    #if no gender data, say no gender data
    try:
        gender = df['Gender'].value_counts()
        print(f'The type of users by gender are: \n{gender}')
    except:
        print('There is no gender data for this city.')

    # Display earliest, most recent, and most common year of birth
    #if no birth year, print no birth year
    try:
        oldest_user = df['Birth Year'].min()
        youngest_user = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode()[0]
        print(f'The oldest user was born in ', oldest_user)
        print(f'The youngest user was born in ', youngest_user)
        print(f'The most common birth year is ', common_birth_year)
    except:
        print('There is no data on birth year for this city.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Takes user input if they would like to view the raw data.
    Loops until they do not want to see any more data."""

    raw_data = input('Would you like to see raw data? \nEnter yes or no: ').lower()
    n = 5
    if raw_data == 'yes':
        print(df.head(n))
        again = 'yes'
    while again == 'yes':
        again = input("Would you like to see more data?\nEnter 'yes' or 'no': ").lower()
        if again == 'yes':
            n += 5
            print(df.head(n))
        elif again != 'yes':
            break

#main runs functions defined above
def main():
    while True:
        city = get_city()
        month, day = get_time_filter()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        print("That was fun!")
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("Goodbye")
            break


if __name__ == "__main__":
	main()
