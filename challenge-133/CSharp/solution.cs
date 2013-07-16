void Main()
{
	Dictionary<int, List<RoomAction>> roomActions = new Dictionary<int, List<RoomAction>>();
	Dictionary<int, RoomSummary> roomSummaries = new Dictionary<int, RoomSummary>();
	
	foreach (string eventLog in File.ReadAllLines(@"input.txt").Skip(1))
	{
		string[] eventData = eventLog.Split(' ');
		int userID = int.Parse(eventData[0]);
		int roomID = int.Parse(eventData[1]);
		string action = eventData[2];
		int timestamp = int.Parse(eventData[3]);
		
		if(roomActions.ContainsKey(roomID))
		{
			if(action == "I")
				roomActions[roomID].Add(new RoomAction {
					UserID = userID,
					Timestamp = timestamp,
					Action = action
				});
			else
			{
				RoomAction inAction = roomActions[roomID].First(a => a.UserID == userID && a.Action == "I");
				int duration = timestamp - inAction.Timestamp + 1;
				
				if(roomSummaries.ContainsKey(roomID))
				{
					RoomSummary summary = roomSummaries[roomID];
					summary.TotalDuration += duration;
					if(!summary.UserIDs.Contains(userID))
						summary.UserIDs.Add(userID);
				}
				else
				{
					roomSummaries.Add(roomID, new RoomSummary {
						TotalDuration = duration,
						UserIDs = new List<int> { userID }
					});
				}
			}
		}
		else
		{
			roomActions.Add(roomID, new List<RoomAction> {
				new RoomAction{
						UserID = userID,
						Timestamp = timestamp,
						Action = action
					}
			});
		}
	}
	
	foreach (KeyValuePair<int, RoomSummary> summary in roomSummaries.OrderBy (s => s.Key))
	{
		string.Format("Room {0}, {1} minute average visit, {2} visitor total", summary.Key, summary.Value.TotalDuration / summary.Value.UserIDs.Count, summary.Value.UserIDs.Count).Dump();
	}
}

public class RoomAction
{
	public int UserID { get; set; }
	public int Timestamp { get; set; }
	public string Action { get; set; }
}

public class RoomSummary
{
	public List<int> UserIDs { get; set; }
	public int TotalDuration { get; set; }
}