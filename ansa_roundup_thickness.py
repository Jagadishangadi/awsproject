import ansa
from ansa import base, constants, guiTk

def main():

    # Create window
    w = guiTk.DOWindowCreate("PROPERTY THICKNESS VIEWER", guiTk.constants.DOExitDestroy)

    # Create table with 6 columns
    table = guiTk.DOTableCreate(w, 0, 6)
    guiTk.DOTableHeaderSetLabel(table, guiTk.constants.DOHorizontal, 0, "ID")
    guiTk.DOTableHeaderSetLabel(table, guiTk.constants.DOHorizontal, 1, "Name")
    guiTk.DOTableHeaderSetLabel(table, guiTk.constants.DOHorizontal, 2, "T1 (Original)")
    guiTk.DOTableHeaderSetLabel(table, guiTk.constants.DOHorizontal, 3, "T1 (Rounded)")
    guiTk.DOTableHeaderSetLabel(table, guiTk.constants.DOHorizontal, 4, "Rounding")
    guiTk.DOTableHeaderSetLabel(table, guiTk.constants.DOHorizontal, 5, "STATUS")
    guiTk.DOTableSetColumnAcceptText(table, 5, True)

    # Collect LS-DYNA PROPERTIES
    pid_list = base.CollectEntities(constants.LSDYNA, None, "PROPERTIES", recursive=True)
    pid_list = sorted(list(pid_list), key=lambda x: x._id)

    row = 0

    for each_pid in pid_list:

        # Read name
        name = base.GetEntityCardValues(constants.LSDYNA, each_pid, ("name",)).get("name", "")

        # Read T1
        t1_val = base.GetEntityCardValues(constants.LSDYNA, each_pid, ("T1",)).get("T1", "")

        # Convert safely
        try:
            t1_float = float(t1_val)
        except:
            t1_float = 0.0

        # Rounded value (same as screenshot logic)
        t1_round = round(t1_float, 2)

        # Status logic
        status = "Good"
        if abs(t1_float - t1_round) > 1e-6:
            status = "Rounding"

        # Add row to table
        guiTk.DOTableSetRow(table, row, 0, each_pid._id)
        guiTk.DOTableSetRow(table, row, 1, str(name))
        guiTk.DOTableSetRow(table, row, 2, str(t1_val))
        guiTk.DOTableSetRow(table, row, 3, str(t1_round))
        guiTk.DOTableSetRow(table, row, 4, "Round to 2 decimals")
        guiTk.DOTableSetRow(table, row, 5, status)

        row += 1

    # ACCEPT button logic
    def on_accept(dialog, data):
        for r in range(row):
            pid_id = int(float(guiTk.DOTableText(table, r, 0)))
            rounded_val = float(guiTk.DOTableText(table, r, 3))

            for each_pid in pid_list:
                if each_pid._id == pid_id:
                    base.SetEntityCardValues(constants.LSDYNA, each_pid, ("T1", rounded_val))

        guiTk.DOExitDestroy(w)

    accept_btn = guiTk.DOPushButtonCreate(w, "ACCEPT", on_accept, None)
    guiTk.DOSetBackgroundColor(accept_btn, 0, 255, 0)

    # REJECT button logic
    def on_reject(dialog, data):
        guiTk.DOMessageBoxShow("Confirm Rejection",
                               "Are you sure you want to reject and close the window?",
                               guiTk.constants.DOMessageBoxYesNo)
        guiTk.DOExitDestroy(w)

    reject_btn = guiTk.DOPushButtonCreate(w, "REJECT", on_reject, None)
    guiTk.DOSetBackgroundColor(reject_btn, 255, 0, 0)

if __name__ == "__main__":
    main()