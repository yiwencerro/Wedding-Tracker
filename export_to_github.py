#!/usr/bin/env python3
"""
Export wedding planner tasks to GitHub Projects CSV format.
This script reads the task data from the HTML file and generates a CSV
that can be imported directly into GitHub Projects.
"""

import csv
import json
import re
from datetime import datetime
from pathlib import Path

# Task data (copied from the HTML wedding planner)
TASKS = [
    ("Call florist — discuss bridal bouquet", "Vendors", "In progress", "Yiwen", "2026-05-11", "2026-05-22", "Found her — connect this week"),
    ("Confirm + contract bartender", "Vendors", "To do", "Yiwen", "2026-05-11", "2026-05-22", "You have someone in mind — lock her in now!"),
    ("Book luxury portable bathroom rental", "Venue", "To do", "Michael", "2026-05-11", "2026-05-22", "Bellport Inn plumbing can't handle 60+ guests"),
    ("Find + book videographer", "Vendors", "To do", "Both", "2026-05-11", "2026-06-05", "Fall dates book up fast"),
    ("Confirm bridesmaids ordered dresses", "Attire", "In progress", "Yiwen", "2026-05-11", "2026-06-22", "Color sent — set a hard deadline"),
    ("Book rehearsal dinner restaurant", "Events", "To do", "Both", "2026-05-18", "2026-06-12", "Bellport spots for ~20+ incl. China family"),
    ("Research projector rental for dad's video", "Logistics", "To do", "Michael", "2026-05-18", "2026-06-05", "Test outdoor AV — daylight visibility"),
    ("Confirm cousin DJ setup (speakers etc.)", "Music", "To do", "Michael", "2026-05-18", "2026-08-01", "Outdoor sound testing needed"),
    ("Finalize China family rental car (9 ppl)", "Guests", "To do", "Yiwen", "2026-05-25", "2026-06-12", "Book minivan/SUV before summer rates peak"),
    ("Start runner's tan treatment", "Beauty", "To do", "Yiwen", "2026-05-25", "2026-09-15", "Gradual self-tanner to blend tan lines for makeup day"),
    ("Build ceremony music playlist", "Music", "To do", "Both", "2026-06-01", "2026-08-01", "Processional, dinner, first dance, parent dances"),
    ("Confirm EU guests' final headcount", "Guests", "To do", "Michael", "2026-06-01", "2026-08-31", "Needed for seating + catering"),
    ("Decoration trial (arch + waterfall flowers)", "Decor", "To do", "Yiwen", "2026-06-08", "2026-07-31", "Test setup, photograph layout for reference"),
    ("Work with Father Bill on ceremony details", "Ceremony", "To do", "Both", "2026-06-08", "2026-08-15", "Readings, music, vow exchange, walking order"),
    ("Buy men's ties + own wedding shoes", "Attire", "To do", "Both", "2026-06-15", "2026-07-12", "Groom + groomsmen ties; your shoes"),
    ("Flower girl + ring bearer attire", "Attire", "To do", "Both", "2026-06-15", "2026-08-01", "Outfits + rehearsal prep for the kids"),
    ("Hard check-in: maids have their dresses", "Attire", "To do", "Yiwen", "2026-06-22", "2026-06-26", "Don't leave this until August"),
    ("Book Asheville honeymoon hotel", "Honeymoon", "To do", "Both", "2026-06-29", "2026-08-22", "Target: confirmed before Aug 22"),
    ("Bachelor party", "Events", "In progress", "Michael", "2026-07-06", "2026-07-17", "Mid-July — all booked, enjoy!"),
    ("Decor trial at Bellport Inn backyard", "Decor", "To do", "Yiwen", "2026-07-06", "2026-07-31", "Arch door, waterfall, table dry arrangements"),
    ("Online MUA call — styles + tan brief", "Beauty", "To do", "Yiwen", "2026-07-13", "2026-07-24", "Discuss runner's tan, each person's look"),
    ("Finalize Asheville transport + activities", "Honeymoon", "To do", "Michael", "2026-07-13", "2026-08-22", "Before Aug 22 deadline"),
    ("Confirm liquor quantities with bartender", "Vendors", "To do", "Michael", "2026-07-20", "2026-08-14", "Calculate for 60–65 guests"),
    ("Design bilingual menus + name cards", "Decor", "To do", "Yiwen", "2026-07-20", "2026-08-17", "Chinese + English — allow print lead time"),
    ("Draft ceremony program (bilingual)", "Ceremony", "To do", "Yiwen", "2026-07-27", "2026-08-14", "Include Father Bill's sections"),
    ("Finalize all Asheville bookings by 8/22", "Honeymoon", "To do", "Both", "2026-08-03", "2026-08-22", "Hard deadline — hotel + transport"),
    ("Finalize vendor meal counts", "Vendors", "To do", "Yiwen", "2026-08-03", "2026-09-04", "Bartender, 5 MUA artists, photographers, coordinator"),
    ("Husband's church documents ready", "Admin", "To do", "Michael", "2026-08-10", "2026-09-11", "Confirm exact docs needed with Father Bill"),
    ("Schedule first dress fitting + alteration", "Attire", "To do", "Yiwen", "2026-08-10", "2026-08-28", "Even bought dresses benefit from alterations"),
    ("Send menus + name cards to print", "Decor", "To do", "Yiwen", "2026-08-17", "2026-08-28", "Allow 2–3 weeks in case of reprints"),
    ("Confirm speech givers", "Ceremony", "To do", "Both", "2026-08-17", "2026-08-28", "Cue dad's video moment in the timeline"),
    ("Brief MUA team in writing", "Beauty", "To do", "Yiwen", "2026-08-17", "2026-08-28", "Inspo photos, runner's tan notes, each look"),
    ("Send day-of timeline draft to JME Planner", "Logistics", "To do", "Both", "2026-08-24", "2026-09-04", "Cottage → church → marina → cocktails → dinner"),
    ("Place liquor order", "Vendors", "To do", "Michael", "2026-08-24", "2026-09-11", "Coordinate delivery with venue + bartender"),
    ("Contact MIA guests + confirm EU count", "Guests", "To do", "Michael", "2026-08-31", "2026-09-11", "Needed for final catering number"),
    ("Give final guest count to caterer + venue", "Vendors", "To do", "Yiwen", "2026-08-31", "2026-09-11", "60–65 guests confirmed"),
    ("Give photographer must-have shot list", "Vendors", "To do", "Yiwen", "2026-09-07", "2026-09-14", "Cultural moments, dog w/ Insta360, family groups"),
    ("Finalize seating chart + escort cards", "Logistics", "To do", "Yiwen", "2026-09-07", "2026-09-14", "Share copy with JME Planner"),
    ("Finalize floor plan + send to venue", "Logistics", "To do", "Both", "2026-09-07", "2026-09-14", "Include projector, bar area, dog-friendly zone"),
    ("Finalize music playlist → send to cousin", "Music", "To do", "Michael", "2026-09-07", "2026-09-14", "All ceremony + reception songs confirmed"),
    ("Schedule decor drop-off with venue", "Venue", "To do", "Yiwen", "2026-09-07", "2026-09-14", "Arch, waterfall, dry flowers, mugs + candy favors"),
    ("Final dress fitting + alterations", "Attire", "To do", "Yiwen", "2026-09-14", "2026-09-18", "Start breaking in your wedding shoes now!"),
    ("Confirm all vendor arrival times", "Vendors", "To do", "Both", "2026-09-14", "2026-09-18", "Photographers, MUA team, bartender, rentals"),
    ("Send timeline to bridal party + family", "Logistics", "To do", "Both", "2026-09-14", "2026-09-18", "Include EU + China family day logistics"),
    ("Create welcome bags (China + EU guests)", "Guests", "To do", "Yiwen", "2026-09-14", "2026-09-18", "Small gesture for international guests"),
    ("Final venue walkthrough with JME Planner", "Venue", "To do", "Both", "2026-09-14", "2026-09-18", "Layout, decor, vendor logistics"),
    ("Targeted self-tanner for tan lines", "Beauty", "To do", "Yiwen", "2026-09-14", "2026-09-24", "7–10 days out — blend runner's tan lines"),
    ("Bridal party group text + planner info", "Logistics", "To do", "Yiwen", "2026-09-19", "2026-09-24", "Wedding day questions go to JME Planner"),
    ("Confirm ceremony rehearsal details", "Ceremony", "To do", "Both", "2026-09-19", "2026-09-24", "Date, time, location, walking order"),
    ("Email all vendors — final timeline", "Vendors", "To do", "Both", "2026-09-19", "2026-09-24", "Everyone gets the same document"),
    ("Have dresses steamed", "Attire", "To do", "Yiwen", "2026-09-19", "2026-09-24", "Dress + all bridesmaid dresses"),
    ("Manicure + pedicure", "Beauty", "To do", "Yiwen", "2026-09-23", "2026-09-25", "2–3 days before the wedding"),
    ("Pick up all formalwear", "Attire", "To do", "Michael", "2026-09-23", "2026-09-25", "Confirm wedding party has theirs too"),
    ("Drop off welcome gifts to guests", "Guests", "To do", "Both", "2026-09-23", "2026-09-25", "China family Airbnb + EU guests"),
    ("Prepare vendor gratuity envelopes", "Admin", "To do", "Both", "2026-09-23", "2026-09-25", "Seal + sign on the seal line"),
    ("Order wedding morning breakfast/lunch", "Logistics", "To do", "Yiwen", "2026-09-23", "2026-09-25", "For getting-ready crew at Bellport cottage"),
    ("Pack for Asheville honeymoon", "Honeymoon", "To do", "Both", "2026-09-23", "2026-09-25", ""),
    ("Ceremony rehearsal + rehearsal dinner", "Events", "To do", "Both", "2026-09-25", "2026-09-25", "Church rehearsal separate from dinner"),
    ("Pack wedding detail box for photographer", "Logistics", "To do", "Yiwen", "2026-09-25", "2026-09-25", "Rings, vow books, veil, jewelry, dog's Insta360!"),
    ("WEDDING DAY — September 26!", "Wedding Day", "To do", "Both", "2026-09-26", "2026-09-26", "Eat breakfast, stay hydrated, enjoy every minute"),
    ("Send thank you cards to guests", "Admin", "To do", "Both", "2026-09-28", "2026-10-03", ""),
    ("Return formalwear + rentals", "Admin", "To do", "Michael", "2026-09-28", "2026-10-03", ""),
    ("Preserve dress + bouquet", "Personal", "To do", "Yiwen", "2026-09-28", "2026-10-03", ""),
    ("Enjoy the Asheville honeymoon!", "Honeymoon", "To do", "Both", "2026-09-28", "2026-10-03", "You did it!"),
]

def calculate_priority(due_date_str):
    """Assign priority based on due date"""
    try:
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
        days_left = (due_date - datetime.now()).days
        if days_left < 0:
            return "Past due"
        elif days_left <= 7:
            return "Urgent"
        elif days_left <= 30:
            return "High"
        else:
            return "Medium"
    except:
        return "Medium"

def status_map(status):
    """Map status to GitHub Projects format"""
    mapping = {
        "To do": "Todo",
        "In progress": "In Progress",
        "Done": "Done",
    }
    return mapping.get(status, status)

def create_csv(output_path="wedding_planner.csv"):
    """Generate GitHub Projects CSV"""
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        
        # GitHub Projects header row
        writer.writerow([
            "Title",
            "Status",
            "Priority",
            "Labels",
            "Assignees",
            "Due date",
            "Description"
        ])
        
        # Write tasks
        for task_name, category, status, owner, start_date, due_date, note in TASKS:
            priority = calculate_priority(due_date)
            
            # Format dates as MM/DD/YYYY for GitHub
            due_date_fmt = datetime.strptime(due_date, "%Y-%m-%d").strftime("%m/%d/%Y")
            
            # Combine category and owner as labels
            labels = f"{category},{owner}"
            
            # Status mapping
            gh_status = status_map(status)
            
            # Description includes the note
            description = note if note else ""
            
            writer.writerow([
                task_name,
                gh_status,
                priority,
                labels,
                owner if owner != "Both" else "Yiwen,Michael",
                due_date_fmt,
                description
            ])
    
    return output_path

if __name__ == "__main__":
    csv_file = create_csv()
    print(f"✅ CSV exported to: {csv_file}")
    print(f"📊 Total tasks: {len(TASKS)}")
    print("\n📋 Next steps:")
    print("1. Go to your GitHub repo → Projects tab")
    print("2. Create a new Project (or open existing)")
    print("3. Click menu (⋯) → Import items")
    print("4. Upload this CSV file")
    print("\n💡 The CSV includes:")
    print("   • Task titles")
    print("   • Status (Todo, In Progress, Done)")
    print("   • Priority (Urgent, High, Medium)")
    print("   • Category + Owner as labels")
    print("   • Assignees (Yiwen/Michael/Both)")
    print("   • Due dates")
    print("   • Descriptions")
