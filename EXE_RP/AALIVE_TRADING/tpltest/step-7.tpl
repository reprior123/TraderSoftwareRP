 
    <div class="step">
            <div class="moduleTitle hd">
                    <h2>{$APP.LBL_CR_INVESTOR_PROFILE} - {$APP.LBL_CR_LEGAL_ENTITIES}</h2>
                    <h3>{$APP.LBL_CR_INVESTMENT_GUIDELINES} - {$APP.LBL_CR_STEP} 7</h3>
                    <div class="clear"></div>
            </div>
            <div class="row portfolio-overview">
                    <div class="small-12 column">
                            <p><b>{$APP.LBL_PLANNED_COST_OUTLAYS}</b><br><br>
                            </p>
                            <form class="step_form">
                                    <p>
    <input type="radio" name="planned_cost_outlays" value="ja, im Umfang von > 30% des investierten Vermoegens" {if $data->planned_cost_outlays eq "ja, im Umfang von > 30% des investierten Vermoegens"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_7_1_TEXT}<br>
    <input type="radio" name="planned_cost_outlays" value="ja, im Umfang von 10% - 30% des investierten Vermoegens" {if $data->planned_cost_outlays eq "ja, im Umfang von 10% - 30% des investierten Vermoegens"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_7_2_TEXT}<br>
    <input type="radio" name="planned_cost_outlays" value="nein, oder im Umfang von < 10% des investierten Vermoegens" {if $data->planned_cost_outlays eq "nein, oder im Umfang von < 10% des investierten Vermoegens"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_7_3_TEXT}<br>
    <input type="radio" name="planned_cost_outlays" value="falls ja, welche" {if $data->planned_cost_outlays eq "falls ja, welche"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_7_4_TEXT}<br>
                                    </p>
                            </form>
                    </div>
            </div>
            <a href="javascript:void(0)" onclick="SUGAR.RiskWorkflow.next()" data-step="8" class="button gen-button next" >{$APP.LBL_CR_NEXT}</a>
    </div> 
