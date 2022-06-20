import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    print('hello there, let\'s discover some us bike statectics')      
        # input collction
        # Validate the the choice is as expected
    while True:
        city = input("please enter a city name from the above mentioned: \n\n").lower()
        if city in CITY_DATA:
            break
        else:
            print("wrong entry ,please try again!")
              
    # get user input for month   
    months = ['january', 'february', 'march', 'april', 'may', 'june','all']    
    while True:
        month = input("\n\nto select a spacific month, please enter a month from the first half of the year or all for no filter: \n\n").lower()
        if month  in months:
            break
        else:
            print("wrong entry ,please try again!")    
            
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday','all']
    while True:
        day = input("\n\nto select a spacific day, please enter the chosen day or all for no filter: \n\n").lower()
        if day  in days:
            break
        else:
            print("wrong entry ,please try again!")
    print('-'*40) 
    
    return city, month ,day   
    
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df= pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()

    df['day_of_week'] = df['Start Time'].dt.day_name()


    # filter by month if applicable
    if month != 'all':
        # # # use the index of the months list to get the corresponding month name
        months = ['january', 'february', 'march', 'april', 'may', 'june','all']    
        # filter by month to create the new dataframe
        df = df[df['month']== month.title()]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] ==day.title()]
    
    return df   

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    
    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("\nMost Popular month:" , popular_month)
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("\nMost Popular Day:" , popular_day)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("\nMost Popular hour:" , popular_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    the_common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station:" , the_common_start_station)
    
    # display most commonly used end station
    the_common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station: " , the_common_end_station )

    # display most frequent combination of start station and end station trip
    df['route'] = df['Start Station']+"-"+df['End Station']
    the_most_frequent_combination = df['route'].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)   

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time_in_total = df['Trip Duration'].sum()
    print('Total Travel Time:', travel_time_in_total)
    # TO DO: display mean travel time
    mean_of_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean_of_travel_time)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)   

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...')
    start_time = time.time()

    # Display counts of user types
    print('Type stats of user :')
    print(df['User Type'].value_counts())
    gender_count =None
    if 'Gender'  in df.columns and "Birth Year" in df.columns:
        try:
            gender_count= df['Gender'].value_counts().to_frame()
            print('Gender stats of user:', gender_count)
        
    # Display earliest, most recent, and most common year of birth
            print('Year of birth stats:')
            earliest_year = df['Birth Year'].min()
            print('Earliest year of birth: \n',earliest_year)
    
            most_recent_year = df['Birth Year'].max()
            print('Most recent year of birth: \n',most_recent_year)

            most_common_year = df['Birth Year'].mode()[0]
            print('Most common year of birth: \n', most_common_year)
        except KeyError:
            print("This data is not available for Washington")
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    
    
def main():
    while True:
        city, month , day = get_filters()
        df = load_data(city, month, day) 
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()