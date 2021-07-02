#include<bits/stdc++.h>
const double PI = atan2(0,-1);

using namespace std;

struct point{
    double x, y;
    point(double x_, double y_) : x(x_),y(y_){}

    point operator+(point other){
        return point(x +other.x,y +other.y);
    }
    point operator-(point other){
        return point(x-other.x,y-other.y);
    }

    double len(){
        return sqrt(x*x+y*y);
    }

};
ostream& operator<<(ostream& o, point p){
    o<< "(" << p.x<<", "<<p.y<<")";
    return o;
};
double cross(point p1, point p2){
    return p1.x*p2.y - p1.y*p2.x;
}
double dot(point p1, point p2){
    return p1.x*p2.x + p1.y*p2.y;
}

double angle_between_vectors(point v1, point v2){
    return atan2(cross(v1,v2),dot(v1,v2));
}


double triangle_area(point a, point b, point c){
    point v1 = b-a;
    point v2 = c-a;
    return abs(cross(v1,v2)/2);
}

double area_of_polygon(vector<point> poly){
    double s=0;
    //cout<<" size of "<< poly.size()<<"\n";
    for (int i=0;i<poly.size();i++){
        int next = (i+1)% poly.size();
        s+= cross(poly[i],poly[next]);
    }
    return abs(s/2);
}

bool is_polygon_convex(vector<point> poly){
    double s = 0;
    for (int i=0;i<poly.size();++i){
        int j = (i+1)%poly.size();
        int k = (j+1)%poly.size();
        if (cross(poly[j]-poly[i],poly[k]-poly[j])<=0){
            return false;
        }
        s += angle_between_vectors(poly[j]-poly[i],poly[k]-poly[j]);
    }

    if (abs(s-2*PI)<0.1){
        return true;
    }
    return false;

}


struct line{
    double a,b,c;
    line(point p1,point p2){
        a = p2.y - p1.y;
        b = p1.x - p2.x;
        c = -(a*p1.x + b*p1.y);
        assert(abs(a*p2.x + b*p2.y +c)<= 1e-9);
        double tmp = sqrt(a*a+b*b);
        a/=tmp;
        b/=tmp;
        c/=tmp;
    }

    double dist(point p){
        return a*p.x+b*p.y+c;
    }
    
};
bool is_parallel(line l1, line l2){
    return abs(l1.a*l2.b - l1.b*l2.a)<=1e-9;
}
point intersection(line l1, line l2){
    double d = l1.a*l2.b - l1.b*l2.a;
    double nx = -l1.c*l2.b + l1.b*l2.c;
    double ny = -l1.a *l2.c + l1.c*l2.a;
    return point(nx/d,ny/d);
}

bool point_in_line(point A,point B,point C){
    if (abs(cross(B-C,A-C))<=1e-9){
        if (min(B.x,C.x)<=A.x && A.x<=max(B.x,C.x) && min(B.y,C.y)<=A.y && A.y<=max(B.y,C.y))
            return true;
        else
            return false;
    }
    else{
        return false;
    }
}
int main(){

    double x1,y1,x2,y2,x3,y3;
    cin>>x1>>y1>>x2>>y2>>x3>>y3;
    std::cout << std::setprecision(7);
    point A(x1,y1);
    point B(x2,y2);
    point C(x3,y3);

    line l(B,C);

    double dis = l.dist(A);

    point v_line = C-B;
    point unit_vector(-(v_line.y/v_line.len()),v_line.x/v_line.len());

    point dist_vector(unit_vector.x*dis,unit_vector.y*dis);

    point X = A+dist_vector;

    if (point_in_line(X,B,C)){
        cout<<abs(dis)<<endl;
    }
    else{
        point A_B = A-B;
        point A_C = A-C;
        cout<<min(abs(A_B.len()),abs(A_C.len()))<<endl;
    }    
}
