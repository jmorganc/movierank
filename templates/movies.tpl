%rebase('templates/layout.tpl', title='Movies', active_home='class="active"')
        <div class="page-header">
            <h1>Movies</h1>
        </div>

        <div class="row">
            <div class="col-md-12">
                See what movies are available and add them to your collection.
            </div>
        </div>

        <div class="row">
            <div class="col-md-12">
                %for movie in movies:
                <div class="movie">
                    <strong>{{movie['title']}}</strong><br/>
                    <strong>ID: </strong>{{movie['id']}}<br/>
                    <strong>In collection: </strong>{{movie['in_collection']}}<br/>
                    %if movie['in_collection']:
                    <a href="javascript:void(0);">Remove</a>
                    %else:
                    <a href="javascript:void(0);">Add</a>
                    %end
                </div>
                %end
            </div>
        </div>