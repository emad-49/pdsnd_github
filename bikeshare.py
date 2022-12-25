import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid input
         city = input(' Choose City to starte analyize?\n') 
         city = city.lower()
         if city not in ['chicago','new york city','washington']:
                print("please Enter a correct City")
         else:
            break 
         
    while True:
        month = input(' Choose month to fillter ?\n') 
        if month not in ['january', 'february', 'march', 'april', 'may', 'june','all']:
            print("Please Enter a correct month ")
        else:
            break
        
    while True:
        day =  input(' Choose day to fillter ?\n') 
        if day not in ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'all']:
             print("pleas Enter correct day")
        else:
            break
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    
    print("This is the most common month",  popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("This is the most common day of the week", popular_day)

    # TO DO: display the most common start hour
    
    df['hour'] = df['Start Time'].dt.hour #Convert to hour 
    popular_hour = df['hour'].mode()[0]
   
    print("This is the most common  start hour", popular_day)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
#     df['column_name'].value_counts()
    start_station = df['Start Station'].value_counts().idxmax()
    
    print("this is the  commonly used start station", start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print("this is the  commonly used end station", end_station )

    # TO DO: display most frequent combination of start station and end station trip
    
    cmbination_station = df.groupby(['Start Station', 'End Station']).count()
    print('most commonly used end station', cmbination_station)

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = (df['Trip Duration']).sum()
    
    print('total traval time',  total_travel_time)


    # TO DO: display mean travel time
    
    mean_travel_time = (df['Trip Duration']).mean()
    print('AVG traval time', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        user_type = df['User Type'].value_counts()
        print('the count of the users types', user_type)
    except KeyError:
        print("There is no user type for this city")
    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('the count of the users Gender', gender)
    except KeyError:
        print("There is no Gnder information for this city")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth = df['Birth Year'].min()
        print('user earliest birth day', earliest_birth)
        most_birth = df['Birth Year'].max()
        print('user most birth day', most_birth )
        common_birth =  df['Birth Year'].value_counts().idxmax()
        print('user common  birth day',common_birth )
    except KeyError:
        print("There is No Data for this city")
    
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def display_data(df):
    
    """ Function To Aske the user to Display the  5 rows of data Stata  """
    
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while (view_data == 'yes'):
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower() 


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
