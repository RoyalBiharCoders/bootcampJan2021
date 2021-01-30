/*Created by: Prashantkr -- "GHAT ALLOCATION SYSTEM"(27 - 01 - 2021)
The code is written in c language and runs Ghat Allocation System.
As this code is the very first attempt, it might have loopholes and if you know how to improve it, you can take it forward!*/
#include <stdio.h>

int main(){
    int gseat[4] = {10,40,20,30};
    int seat, ghat;//seat for taking seats wanted and ghat for choosing ghat number.

    printf("Select an option from the following ghats:\n1)Ghat1\n2)Ghat2\n3)Ghat3\n4)Ghat4\n");
    scanf("%d", &ghat);

    printf("Seat available in Ghat%d is:\t %d\n", ghat, gseat[ghat-1]); //gseat[ghat-1] because input wil be 1 more than the list indexing as indexing starts from 0!

	//Now, while loop will run untill the list gseat has elements which is greater than 0.
	
    while(gseat[ghat] > 0){
        printf("\nEnter seats wanted:\t \n");
        scanf("%d", &seat);

		//now, checking if seat entered is lesser than the seat available and seat entered is greater than or equal to 0. If conditions met, the seat entered is subt from list.
		
        if(seat < gseat[ghat-1] && seat >= 0){
            gseat[ghat - 1] = gseat[ghat - 1] - seat;
            printf("Seat alloted\n");
            printf("Remaining seats:\t%d\n", gseat[ghat - 1]);
        }

		//Now, it checks if seat entered and seat available is 1! If so, seat is alloted!
		
        else if(seat == 1 && gseat[ghat - 1] == 1){
            gseat[ghat - 1] -= 1;
            printf("Alloted!\n");
            printf("No remaining seats avialble in Ghat%d!\nRemaining seats: %d", ghat, gseat[ghat - 1]);
        }
		
		//if seat entered is greater than the available seats, the user is asked to choose from another ghat whose seat is within the requirement. 
		
        else if(seat > gseat[ghat - 1]){
            printf("Choose from another ghats.\n");

			//for loop prints the seats available in the respective ghat.
			
            for (int i = 0; i<4 ; i++){
                if(gseat[i] > 1){
                    printf("Ghat%d has seats: %d\n", i+1, gseat[i]);
                }
                
            }
            printf("Enter Ghat number from above option with appropriate seats:\t\n");
            scanf("%d", &ghat);

            printf("Enter seats required in the selected ghat: \n");
            scanf("%d", &seat);

            gseat[ghat - 1] -= seat;
            printf("Seat Alloted!\n");
            printf("Remaining seats available in Ghat%d: %d\n",ghat, gseat[ghat - 1]);
        }
        else{
            
            printf("Enter valid command.\n");
        }


    }
	//this for loop is of no use as per my considerations
    // for(int j = 0; j < 4; j++){
    //             if(ghat[j] == 0){
    //                 printf("Ghat%d has seats: %d\n", j+1, ghat[j]);
    //             }
    //             printf("No Seats avilable now!");
    //             break;
    //         }
    return 0;
}
