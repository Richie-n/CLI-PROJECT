from lib.songs import Songs
from lib.artist import Artist
from lib.artist_song import ArtistSong
from lib.reviews import Reviews
import sys


def main_menu():
    while True:

        print('x=x=x=x=x=x=x=x=x=x=x=x=MAIN MENU=x=x=x=x=x=x=x=x=x=x=x=x')
        print('1.Manage Artists')
        print('2.Manage Songs')
        print('3.Manage Reviews')
        print('4.Exit')

        choice = input('\nEnter your choice: ')
        if choice == '1':
            return artist_operations()
        elif choice == '2':
            return song_operations()
        elif choice == '3':
            return review_operations()
        elif choice == '4':
            sys.exit()
        else:
            print('Invalid choice')
            

def artist_operations():
       while True:

        print('\n<---------------------ARTIST MENU--------------------->')
        print('1.Create Artist:')
        print('2.Fetch Artist by ID:')
        print('3.Update Artist:')
        print('4.Delete Artist:')
        print('5.List All Artists:')
        print('6.Match Artist with song:')
        print('7.List an Artists songs:')
        print('8.Artist Collabs:')
        print('9.Total Number of Artists:')
        print('10.Main Menu:')

        choice = input('\nEnter your choice: ')
        artist = Artist()
        artist_song = ArtistSong()
        if choice == '1':
            name = input('Enter Name: ')
            genre = input('Enter Genre: ')
            origin = input('Enter Origin: ')
            artist.create(name, genre, origin)
            print(name+f' added successfully')
    
        elif choice == '2':
            id = input('Enter  Artist ID: ')
            single_artist = artist.fetch_artist(id)
            print(single_artist)

        elif choice == '3':
            id = input('Enter  Artist ID: ')
            name = input('Enter Name: ')
            genre = input('Enter Genre: ')
            origin = input('Enter Origin: ')
            artist.update_artist(id, name, genre, origin)
            print(name+' updated successfully')

        elif choice == '4':
            id = input('Enter  Artist ID: ')
            artist.delete_artist(id)
            print('Artist deleted successfully')

        elif choice == '5':
          all_artists= artist.fetch_all_artists()
          print('\nAll Artists')
          print(all_artists)

        elif choice == '6':
            song_id = input('Enter  Song ID: ')
            artist_id = input('Enter  Artist ID: ')
            artist_songs = artist_song.create(song_id, artist_id)
            print(artist_songs)
            print(f'\n Artist songs:{artist_songs} on ArtistID:{artist_id}')

        elif choice == '7':
            id = input('Enter  Artist ID: ')
            artist_songs = artist_song.fetch_songs_by_artist_id(id)
            print(artist_songs)
            print(f'\n Artist songs:{artist_songs} on ArtistID:{id}')

        elif choice == '8':
            id = input('Enter Song ID: ')
            artist_collabs = artist_song.fetch_artists_by_song_id(id)
            print(artist_collabs)
            print(f'\n Artist collab:{artist_collabs} on SongID:{id}')
       
        elif choice == '9':
            total_artists = artist.total_artists()
            print(f'\n Total Number Of Artists:{total_artists}')

        elif choice == '10':
            return main_menu()
        else:
            print('Invalid Input')    


def song_operations():
    while True:
        print("\n*******SONG MENU********")
        print("1.Add Song:")
        print("2.Update Song:")
        print("3.Fetch all Songs:")
        print("4.Fetch Song by id:")
        print("5.Total Nmber of Songs:")
        print("6.Delete Song:")
        print("7.Return to Main Menu ")

        choose = input("\nEnter your choice: ")
        song = Songs()
        if choose == '1':
            name = input('Enter Name: ')
            album = input('Enter Album: ')
            genre = input('Enter Genre: ')
            song.create_song(name, album, genre)
            print(name+' added successfully')

        elif choose == '2':
            id = input('Enter  Song ID: ')
            name = input('Enter Name: ')
            album = input('Enter Album: ')
            genre = input('Enter Genre: ')
            song.update_song(id, name, album, genre)
            print(name+' updated successfully')

        elif choose == '3':
            all_songs = song.fetch_all_songs()
            print('\nAll Songs')
            print(all_songs)

        elif choose == '4':
           id = input('Enter Song ID: ')
           single_song = song.fetch_song(id)
           print(single_song)


        elif choose == '5':
            total_songs = song.total_songs()
            print(f'\n Total Number Of Songs:{total_songs}')

        elif choose == '6':
           id = input('Enter Song ID: ')
           song.delete_song(id)
           print('Song deleted successfully')

        elif choose == '7':
            return main_menu()
        else:
            print('Invalid Input')


def review_operations():
    while True:
        print("\n*******REVIEW MENU********")
        print("1.Add Review")
        print("2.Update Review")
        print("3.Fetch all Reviews")
        print("4.Fetch Reviews by artist id")
        print("5.Fetch Reviews by song id")
        print("6.Count all Reviews")
        print("7.Delete Review")
        print("8.Retun to main menu")

        choice =input('\nEnter your choice:')
        reviews = Reviews ()
        if choice =="1":
            
            song_id = input("Enter Song ID:")
            artist_id = input('Enter Artist ID:')
            review = input('Enter Review:')
            reviews.create_review(review, song_id, artist_id)
            print('Review added successfully')

        elif choice == '2':
            id = input('\nEnter Review ID:')
            review = input('Enter Review:')
            song_id = input('Enter Song ID:')
            artist_id = input('Enter Artist ID:')
            reviews.update_review(id, review, song_id, artist_id)
            print('\nReview updated successfully')
            
        elif choice == '3':
            all_reviews = reviews.fetch_all_reviews()
            print('\nAll Reviews')
            print(all_reviews)
        elif choice == '4':
            aritst_id = input('Enter Artist ID:')
            reviews_by_artist = reviews.fetch_reviews_by_artist_id(aritst_id)
            print('\nReviews by Artist ID')
            print(reviews_by_artist)
        elif choice == '5':
            song_id = input('Enter Song ID:')
            reviews_for_song = reviews.fetch_reviews_by_song_id(song_id)
            print('\nReviews for Song ID')
            print(reviews_for_song)
        elif choice == '6':
            total_reviews = reviews.total_reviews()
            print(f'\n Total Number Of Reviews:{total_reviews}')
        elif choice == '7':
            id = input('Enter Review ID:')
            reviews.delete_review(id)
            print('Review deleted successfully')
        elif choice == '8':
            return main_menu()
        else:
            print('Invalid Input')

        
        



main_menu()