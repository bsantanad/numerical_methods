/* newton_rasp -- 
 * a program that uses the Newton Raphson method to solve ecuations
 *
 * author: Benjamin Santana
 * date: 31/aug/2020
 *
 */

#include<stdio.h>
#include<math.h>

/* Write the function here*/
double f(double x){
    return sin(2*x)*cos(3*x)+cos(x);
}

double dx(double x){
    return (-3)*sin(2*x)*sin(3*x) + 2*cos(2*x)*cos(3*x) - sin(x);
}
/* -------------------- */


int main(void){
    
    int iter = 20;
    float x0 = 5;
    int i;
    double x, xn, fx, fpx;

    printf("|iter\t|\tx\t|\tf(x)\t|\tf'(x)\t||\n");
    xn = x0;
    for(i=0; i<iter; i++){
        x = xn;
	fx = f(x);
	fpx = dx(x);
        xn = x-(fx/fpx);
	if(isnan(fx)) break;	
        printf("|%d\t|%f\t|%f\t|%f\t|\n",i, x, fx, fpx);	
    }
   
    return 0;
}

