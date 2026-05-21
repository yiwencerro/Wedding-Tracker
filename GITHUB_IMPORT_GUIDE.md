# Import Wedding Planner to GitHub Projects

## Quick Start

1. **Download the CSV file:**
   - `wedding_planner.csv` (included)

2. **Create a GitHub Project:**
   - Go to your GitHub repository
   - Click the **Projects** tab
   - Click **New project**
   - Choose **Table** layout
   - Name it: "Wedding Planning"

3. **Import the CSV:**
   - In your new Project, click the menu icon (⋯) in the top right
   - Select **Import items**
   - Upload `wedding_planner.csv`
   - Click **Import**

## What You Get

The CSV includes all 64 wedding tasks with:

| Field | Example | Purpose |
|-------|---------|---------|
| **Title** | "Call florist — discuss bridal bouquet" | Task name |
| **Status** | Todo, In Progress, Done | Task status |
| **Priority** | Urgent, High, Medium | Based on due date |
| **Labels** | Vendors, Yiwen | Category + Owner |
| **Assignees** | Yiwen or Michael | Who's doing it |
| **Due date** | 05/22/2026 | When it's due |
| **Description** | "Found her — connect this week" | Details/notes |

## After Import

Once imported into GitHub Projects, you can:

✅ **Filter** by Status, Priority, Labels, or Assignees  
✅ **Sort** by due date or priority  
✅ **Group** by owner (Yiwen/Michael/Both)  
✅ **Update** task status with drag-and-drop  
✅ **Collaborate** — Michael can be added as a contributor and view/edit tasks  
✅ **Track** progress with the built-in charts  
✅ **Link** tasks to GitHub issues (optional)  

## Using It Together

1. **Yiwen** logs in and updates her tasks
2. **Michael** logs in and updates his tasks  
3. GitHub Projects syncs automatically — no extra coordination needed
4. You both see real-time progress updates

## Sync Back to the Web App

**Note:** The HTML web app and GitHub Projects are separate. If you make changes in GitHub, you'll need to manually sync them back to the HTML app by:
- Editing the TASKS array in the HTML file, OR
- Exporting a new CSV from GitHub and re-running the Python script to generate an updated HTML

For true two-way sync, you'd need a more complex setup with a shared database, but the CSV approach works great for manual syncs.

## Need More Details?

GitHub Projects docs: https://docs.github.com/en/issues/planning-and-tracking-with-projects

---

**Enjoy organizing your wedding! 💕**
