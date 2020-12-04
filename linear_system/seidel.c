/* a program that uses seidel method to 
 * solve linear system 4x4*/

#include<stdio.h>
#include<math.h>

#define TOLERANCE 1e-9

double fa(double b, double c, double d){
    //return (24-3*b-3*c-3*d)/9;	
    //return (2-4*b-c+5*d)/3;	
    return (17-b+c-2*d)/(-6);
}
double fb(double a,double c, double d){
    //return (17-3*a+2*c+2*d)/10;
    //return (-c-d)/7;
    return (-1-8*c-d)/13;
}
double fc(double a, double b, double d){
    //return (45-3*a+2*b-10*d)/18;
    //return (-1-2*b-5*d)/8;
    return (35-3*a+3*b-d)/7;
}
double fd(double a, double b, double c){
    //return (29-3*a+2*b-10*c)/20; 
    //return (5+a+b-4*c)/9;
    return (9+3*a-2*b+c)/11;
}

int main(void){
	
    int max_it = 100; 
    int i;

    /*intial vector*/
    double a=8;
    double b=-4;
    double c=7;
    double d=5;

    double ak, bk, ck, dk;
    
    printf("x4\t\tx3\t\tx2\t\tx1\n");
    for(i=0; i<max_it; i++){
        printf("%f\t|%f\t|%f\t|%f\t|\n",a,b,c,d);
	
	ak = fa(b,c,d);
	bk = fb(ak,c,d);
	ck = fc(ak,bk,d);
	dk = fd(ak,bk,ck);

	if(fabs(ak-a) < TOLERANCE &&
		fabs(bk-b) < TOLERANCE &&
		fabs(ck-c) < TOLERANCE &&
		fabs(dk-d) < TOLERANCE){
	    
	    printf("Iteration No. %d\n",i);
	    break;
	}

	a = ak;
	b = bk;
	c = ck;
	d = dk;
    }

    return 0;

}

