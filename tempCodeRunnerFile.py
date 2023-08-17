    for wall_obj in wall_list:
            width, height = wall_obj.width, wall_obj.height
            if (wall_obj.x + width >= ghost_obj.x >= wall_obj.x - 50) and (wall_obj.y + height >= ghost_obj.y >= wall_obj.y - 50):
                if ghost_obj.x + ghost_obj.radius <= wall_obj.x or ghost_obj.x - ghost_obj.radius >= wall_obj.x + width:
                    ghost_obj.change_direction_x()
                elif ghost_obj.y + ghost_obj.radius <= wall_obj.y or ghost_obj.y - ghost_obj.radius >= wall_obj.y + height:
                    ghost_obj.change_direction_y()
