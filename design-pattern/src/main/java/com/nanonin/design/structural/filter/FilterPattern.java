package com.nanonin.design.structural.filter;

import java.util.ArrayList;
import java.util.List;

public class FilterPattern {
    public static void main(String[] args) {
        List<Chicken> chickens = new ArrayList<>();
        chickens.add(new Chicken("CK1", COLOR.RED, WIGHT.BIG, SEX.ROOSTER));
        chickens.add(new Chicken("CK2", COLOR.WRITE, WIGHT.BIG, SEX.ROOSTER));
        chickens.add(new Chicken("CK3", COLOR.RED, WIGHT.SMALL, SEX.ROOSTER));
        chickens.add(new Chicken("CK4", COLOR.RED, WIGHT.BIG, SEX.HEN));
        chickens.add(new Chicken("CK5", COLOR.RED, WIGHT.BIG, SEX.HEN));

        Criteria redCriteria = new RedCriteria();
        Criteria roosterCriteria = new RoosterCriteria();
        Criteria henCriteria = new HenCriteria();
        Criteria bigCriteria = new BigCriteria();
        Criteria redAndRoosterCriteria = new AndCriteria(redCriteria, roosterCriteria);
        Criteria redOrRoosterCriteria = new OrCriteria(redCriteria, roosterCriteria);
        Criteria bigOrRoosterCriteria = new OrCriteria(bigCriteria, roosterCriteria);

        System.out.println(redCriteria.meetCriteria(chickens).toString());
        System.out.println(henCriteria.meetCriteria(chickens).toString());
        System.out.println(roosterCriteria.meetCriteria(chickens).toString());
        System.out.println(bigCriteria.meetCriteria(chickens).toString());
        System.out.println(redAndRoosterCriteria.meetCriteria(chickens).toString());
        System.out.println(redOrRoosterCriteria.meetCriteria(chickens).toString());
        System.out.println(bigOrRoosterCriteria.meetCriteria(chickens).toString());
    }
}

enum SEX {
    ROOSTER, HEN
}

enum COLOR {
    RED, WRITE
}

enum WIGHT {
    BIG, SMALL
}

class Chicken {
    private String name;
    private COLOR color;
    private WIGHT wight;
    private SEX sex;

    @Override
    public String toString() {
        return "Chicken{" +
                "name='" + name + '\'' +
                ", color=" + color +
                ", wight=" + wight +
                ", sex=" + sex +
                '}';
    }

    public Chicken(String name, COLOR color, WIGHT wight, SEX sex) {
        this.name = name;
        this.color = color;
        this.wight = wight;
        this.sex = sex;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public COLOR getColor() {
        return color;
    }

    public void setColor(COLOR color) {
        this.color = color;
    }

    public WIGHT getWight() {
        return wight;
    }

    public void setWight(WIGHT wight) {
        this.wight = wight;
    }

    public SEX getSex() {
        return sex;
    }

    public void setSex(SEX sex) {
        this.sex = sex;
    }
}

abstract class Criteria {
    interface CheckIt {
        boolean condition(Chicken chicken);
    }

    List<Chicken> filter(List<Chicken> chickens, CheckIt checkIt) {
        List<Chicken> newChickens = new ArrayList<>();
        for (Chicken chicken : chickens) {
            if (checkIt.condition(chicken)) {
                newChickens.add(chicken);
            }
        }
        return newChickens;
    }

    abstract List<Chicken> meetCriteria(List<Chicken> chickens);
}

class RoosterCriteria extends Criteria {

    @Override
    public List<Chicken> meetCriteria(List<Chicken> chickens) {
        return super.filter(chickens, chicken -> SEX.ROOSTER == chicken.getSex());
    }
}

class HenCriteria extends Criteria {
    @Override
    public List<Chicken> meetCriteria(List<Chicken> chickens) {
        return super.filter(chickens, chicken -> SEX.HEN == chicken.getSex());
    }
}

class RedCriteria extends Criteria {
    @Override
    public List<Chicken> meetCriteria(List<Chicken> chickens) {
        return super.filter(chickens, chicken -> COLOR.RED == chicken.getColor());
    }
}


class BigCriteria extends Criteria {
    @Override
    public List<Chicken> meetCriteria(List<Chicken> chickens) {
        return super.filter(chickens, chicken -> WIGHT.BIG == chicken.getWight());
    }
}

class AndCriteria extends Criteria {

    private final Criteria criteria;
    private final Criteria criteriaOther;

    public AndCriteria(Criteria criteria, Criteria criteriaOther) {
        this.criteria = criteria;
        this.criteriaOther = criteriaOther;
    }

    @Override
    public List<Chicken> meetCriteria(List<Chicken> chickens) {
        List<Chicken> chickensCriteria = criteria.meetCriteria(chickens);
        return criteriaOther.meetCriteria(chickensCriteria);
    }
}

class OrCriteria extends Criteria {

    private final Criteria criteria;
    private final Criteria criteriaOther;

    public OrCriteria(Criteria criteria, Criteria criteriaOther) {
        this.criteria = criteria;
        this.criteriaOther = criteriaOther;
    }

    @Override
    public List<Chicken> meetCriteria(List<Chicken> chickens) {
        List<Chicken> chickensCriteria = criteria.meetCriteria(chickens);
        List<Chicken> chickensCriteriaOther = criteriaOther.meetCriteria(chickens);
        for (Chicken chicken : chickensCriteriaOther) {
            if (!chickensCriteria.contains(chicken))
                chickensCriteria.add(chicken);
        }
        return chickensCriteria;
    }
}
