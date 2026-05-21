# Yiwen & Michael's Wedding Planner 💕

A beautiful, interactive wedding planning tool built with HTML, CSS, and vanilla JavaScript. Track tasks, manage timelines, assign responsibilities, and watch your wedding come together!

**Wedding Date:** September 26, 2026 | **Venue:** Bellport Inn, New York | **Guests:** ~60–65

---

## 🎯 Features

### Task Management
- ✅ **Status Tracking** — Toggle tasks between To do, In progress, and Done
- 📝 **Full Editing** — Edit task names, notes, dates, categories, and assignees
- 🗑️ **Delete & Copy** — Remove tasks or duplicate them for quick templates
- ⏱️ **Drag & Drop Timeline** — Drag bars left/right to reschedule, grab edges to resize

### Assignments & Filtering
- 👥 **Owner Assignments** — Assign tasks to Yiwen, Michael, Both, or custom names
- 🔍 **Smart Filters** — Filter by status, category, owner, or urgency
- 📊 **Progress Tracking** — See completion percentage and upcoming deadlines

### Timeline Management
- 📅 **Gantt Chart** — Visual timeline from May through October
- 👁️ **Smart Archive** — Hide past weeks by default, reveal them with one click
- 🎯 **Current Week Focus** — The week you're in is always the first column
- 📍 **Current Status** — Live undo/redo for all changes

### Collaboration Features
- 🔄 **Keyboard Shortcuts** — Ctrl+Z to undo, Ctrl+Shift+Z to redo
- 💾 **Auto-Save** — All changes save to browser immediately
- 📱 **Mobile Friendly** — Works on phones, tablets, and desktops
- 🖱️ **Touch Drag Support** — Drag bars on touch devices too

---

## 🚀 Getting Started

### Open the Planner
1. Click **[Open index.html](./index.html)** or download and open locally in any web browser
2. No installation, no backend needed — works entirely offline!

### Basic Workflow
1. **Search** — Use the search box to find tasks by name
2. **Filter** — Click status pills (To do, In progress, Done) or select by owner/category
3. **Edit** — Hover over a task and click ✏️ to edit details
4. **Assign** — Click the owner badge to change who's working on it
5. **Reschedule** — Drag the colored bar left/right to move dates
6. **Track Progress** — Watch the stats update as you mark tasks complete

---

## 📋 Timeline Structure

All tasks are organized by **12-month timeline**, broken into:
- **Months 12–9** (May–June) — Venue, vendor bookings, initial planning
- **Months 8–6** (July–August) — Major vendor confirmations, design finalization
- **Months 5–3** (August–September) — Final confirmations, rehearsal prep
- **Months 2–0** (September) — Last-minute details, wedding day

### Current Week
The app automatically shows tasks from **the current week onward**. Past weeks can be revealed with the "Show past weeks" button.

---

## 👥 Responsibilities

### Yiwen's Tasks
- Florals, decoration, design
- Bride-specific (beauty, dress, shoes)
- Guest communication
- Timeline & seating management

### Michael's Tasks
- Groom logistics
- EU guest coordination
- Vendor management (bartender, transportation)
- Tech setup (DJ, projector)

### Both
- Honeymoon planning
- Ceremony coordination
- Family decisions
- Day-of timeline

---

## 🛠️ How to Use Key Features

### Undo/Redo
- **Ctrl+Z** (or Cmd+Z on Mac) — Undo last change
- **Ctrl+Y** or **Ctrl+Shift+Z** — Redo
- A toast appears showing what was undone

### Drag Tasks
- **Click and drag the colored bar** — Move task to different week
- **Drag left/right edges** — Change start or end date
- **Hover to see handles** — Gray edge handles appear on hover
- **Live tooltip** — Shows dates as you drag

### Edit Everything
- Click the **✏️ pencil icon** to open full editor
- Change: task name, notes, category, owner, status, dates
- Delete from here too
- **Ctrl+Enter** saves, **Escape** cancels

### Copy & Paste
- Click the **📋 copy icon** — Task is copied to clipboard
- "Paste as new task" button appears at bottom
- Edit as needed before saving

### Filter & Search
- **Search box** — Real-time filter by task name, notes, or category
- **Owner filter** — Show only Yiwen's, Michael's, or Both's tasks
- **Status pills** — To do, In progress, Done, Urgent
- **Category dropdown** — Filter by Vendors, Attire, Beauty, Music, etc.
- **Combine filters** — E.g., "Yiwen + Urgent"

### Show Past Weeks
- Click **"Show past weeks"** button to reveal archived (completed) weeks
- Past weeks appear grayed out on the left
- All bars are still editable

---

## 💾 Data Persistence

**Your data is saved automatically** in your browser's local storage. This means:
- ✅ All changes persist when you refresh or close
- ✅ Works offline — no internet needed
- ✅ Same device, same data (storage is per-browser)
- ❌ Different device = fresh start (share the link or export CSV)

To back up: Export to [GitHub Projects](#export-to-github-projects) or download the CSV.

---

## 📤 Export to GitHub Projects

Want to sync with GitHub? Download the included `wedding_planner.csv` and:
1. Go to your GitHub repo → **Projects** tab
2. Click **New project** → **Table** layout
3. Click menu (⋯) → **Import items**
4. Upload the CSV
5. Tasks sync to GitHub with status, assignees, due dates, and labels!

See `GITHUB_IMPORT_GUIDE.md` for detailed instructions.

---

## 🎨 Customization

All styling is in the CSS at the top of `index.html`. You can customize:
- **Color palette** — `--sage`, `--blush`, `--gold` variables
- **Font** — Uses `Playfair Display` (serif) and `DM Sans` (body)
- **Column widths** — Task column, owner, category, status, week columns
- **Bar colors** — Each category has its own color in `CAT_COLORS` object

### Adding More Tasks
Edit the `TASKS` array in the JavaScript section:
```javascript
{task:"Your task name",cat:"Category",note:"Optional note",status:"todo",owner:"Yiwen",s:pd(2026,5,11),e:pd(2026,5,22)}
```

---

## 📱 Browser Support

- ✅ Chrome/Edge (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ✅ Mobile browsers (iOS Safari, Chrome Mobile)

---

## 🎁 What's in the Box

```
wedding-planner-repo/
├── index.html                    # Main app (open this!)
├── README.md                     # This file
├── GITHUB_IMPORT_GUIDE.md        # Instructions for GitHub Projects import
├── wedding_planner.csv           # Ready-to-import CSV for GitHub
├── export_to_github.py           # Python script to regenerate CSV
└── ARCHITECTURE.md               # Technical details (optional)
```

---

## 💡 Pro Tips

1. **Use "Urgent" filter** — Shows only tasks due in the next 3 weeks
2. **Ctrl+Z often** — Every action (edit, drag, delete) is undoable
3. **Color-coded owners** — Purple = Yiwen, Blue = Michael, Green = Both
4. **Batch updates** — Edit multiple tasks at once with filtering
5. **Mobile-friendly drags** — Swipe works on phones too!
6. **Keyboard shortcuts** — Escape closes modals, Ctrl+Enter saves edits

---

## 🤝 Collaboration Workflow

### For Yiwen & Michael
1. **Share the link** — Deploy to Netlify or GitHub Pages for live access
2. **Both edit freely** — Changes sync in the browser
3. **No login needed** — Just open and start planning
4. **Export to GitHub** when you want a permanent backup in version control

### For the Wedding Party
- Send them the live link
- They can view the timeline (read-only suggested)
- Print the Gantt for physical copies

---

## 📞 Support & Feedback

- **Found a bug?** Check the browser console (F12) for errors
- **Want a feature?** Edit the HTML/JS or open a GitHub issue
- **Need a backup?** The CSV export keeps everything safe

---

## 📄 License

Built with ❤️ for Yiwen & Michael's wedding. Feel free to fork, modify, and use for your own event!

---

## 🎊 Have a Beautiful Wedding!

*"From vision to celebration in 12 months."*

**September 26, 2026 can't come soon enough! 💕**
