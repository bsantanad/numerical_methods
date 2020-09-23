/* secant -- 
 * a program that uses the Secant method to solve ecuations
 *
 * author: Benjamin Santana
 * date: 01/sept/2020
 *
 */

#include<stdio.h>
#include<math.h>

/* Write the function here*/
double f(double x){
    return sin(2*x)*cos(3*x)+cos(x);
}
/* -------------------- */


int main(void){
   
    
    float xa = -3; 
    float xb = -2;

    int iter = 20;
    int i;
    double xc, fax, fbx;

    printf("|iter\t|\tx\t|\tf(x)\t|\n");
   
    for(i=0; i<iter; i++){ 
	fax = f(xa);
	fbx = f(xb);
	if(isnan(fax)) break;	
        printf("|%d\t|%f\t|%f\t|\n",i, xa, fax);	
        xc = xb - ((fbx)*(xb-xa)/(fbx-fax));
	xa = xb;
	xb = xc;
    }
   
    return 0;
}

