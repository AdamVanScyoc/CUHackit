#ifndef DSERVICELOCAL_H
#define DSERVICELOCAL_H

using namespace std;

struct Log {
	int glucoseLevel;
	int carbIntake;
	int insulinDosage;
	int hour;
	int minute;
	Log(int g, int c, int i, int h, int m) {
		glucoseLevel = g;
		carbIntake = c;
		insulinDosage = i;
		hour = h;
		minute = m;
	}
};

class DServiceLocal{
public:
  DServiceLocal();
  ~DServiceLocal();
};
#endif
