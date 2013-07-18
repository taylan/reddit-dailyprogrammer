    void Main()
    {
        Parameters p = ParseParameters("18 8 32 300 550");
        Random r = new Random();
        List<Event> events = new List<Event>();

        int count = 0;
        while (events.Count < p.EventCount)
        {
            count++;
            int visitorIndex = r.Next(0, p.VisitorCount + 1);
            int randomTimestamp = r.Next(p.MinTimestamp, p.MaxTimestamp);
            if(events.Any (ev => ev.UserID == visitorIndex && randomTimestamp > ev.InTimestamp && randomTimestamp < ev.OutTimestamp))
                continue;

            // if the visitor is still in a room at this random time, we get the index of the element, so we can update the OutTimestamp
            int currentEventIndex = events.FindIndex(ev => ev.UserID == visitorIndex && ev.InTimestamp < randomTimestamp && !ev.OutTimestamp.HasValue);
            // if the visitor will enter this room in the future, we find that event, so we can make sure the user exits this room before entering it again
            Event futureEvent = events.Where(ev => ev.UserID == visitorIndex && ev.InTimestamp > randomTimestamp).OrderBy (ev => ev.InTimestamp).FirstOrDefault();
            
            if(currentEventIndex > -1) // visitor is already visiting a room at this time
            {
                events[currentEventIndex].OutTimestamp = r.Next(randomTimestamp, futureEvent != null ? futureEvent.InTimestamp : p.MaxTimestamp + 1);
            }
            else
            {
                events.Add(new Event
                {
                    UserID = visitorIndex,
                    RoomID = r.Next(0, p.RoomCount + 1),
                    InTimestamp = randomTimestamp,
                    OutTimestamp = r.Next(randomTimestamp, futureEvent != null ? futureEvent.InTimestamp : p.MaxTimestamp + 1)
                });
            }
        }
        
        Console.WriteLine(events.Count * 2);
        foreach (Event ev in events.OrderBy (e => e.RoomID).ThenBy (e => e.InTimestamp))
        {
            Console.WriteLine(ev.ToString());
        }
    }

    public Parameters ParseParameters(string s)
    {
        string[] parameters = s.Split(' ');
        
        return new Parameters {
            EventCount = int.Parse(parameters[0]),
            VisitorCount = int.Parse(parameters[1]),
            RoomCount = int.Parse(parameters[2]),
            MinTimestamp = int.Parse(parameters[3]),
            MaxTimestamp = int.Parse(parameters[4])
        };
    }

    public class Parameters
    {
        public int EventCount { get; set; }
        public int VisitorCount { get; set; }
        public int RoomCount { get; set; }
        public int MinTimestamp { get; set; }
        public int MaxTimestamp { get; set; }
    }

    public class Event
    {
        public int UserID { get; set; }
        public int RoomID { get; set; }
        public int InTimestamp { get; set; }
        public int? OutTimestamp { get; set; }
        
        public override    string ToString()
        {
            return string.Format("{0} {1} I {2}{4}{0} {1} O {3}", this.UserID, this.RoomID, this.InTimestamp, this.OutTimestamp, Environment.NewLine);
        }
    }
